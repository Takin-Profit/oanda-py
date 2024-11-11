import ast
import asyncio
import re
from pathlib import Path

import aiofiles

SCRIPT_DIR = Path(__file__).parent
PKG_NAME = "oanda_v20_client"
INPUT_DIR = SCRIPT_DIR / PKG_NAME / "src" / PKG_NAME / "models"
OUTPUT_DIR = SCRIPT_DIR / PKG_NAME / "src" / PKG_NAME / "dataclasses"


def fix_docstring(docstring: str | None) -> str | None:
    """Fix type references in docstrings."""
    if not docstring:
        return docstring
    # Replace Union[Unset, X] with Optional[X] in docstrings
    return docstring.replace("Union[Unset, ", "Optional[")


def get_imports_from_tree(tree: ast.AST) -> list[str]:
    imports = set()  # Changed to set to prevent duplicates
    typing_imports = set()  # Separate set for typing imports

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module:
                names = ", ".join(n.name for n in node.names)
                if node.module == "typing":
                    typing_imports.add(f"from typing import {names}")
                elif "models." in node.module:
                    imports.add(f"from .{node.module.split('.')[-1]} import {names}")
                elif node.module != "types":  # Skip types imports
                    imports.add(f"from {node.module} import {names}")
        elif isinstance(node, ast.Import):
            for name in node.names:
                imports.add(f"import {name.name}")

    # Merge typing imports
    typing_names = set()
    for imp in typing_imports:
        names = imp.replace("from typing import ", "").split(", ")
        typing_names.update(names)

    # Remove Dict and Any as they're in default imports
    typing_names.discard("Dict")
    typing_names.discard("Any")

    # Always include Optional in typing imports
    typing_names.add("Optional")

    if typing_names:
        imports.add(f"from typing import {', '.join(sorted(typing_names))}")

    return sorted(imports)


async def generate_dataclasses(input_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "__init__.py").touch()

    tasks = [
        process_file(file, output_dir)
        for file in input_dir.rglob("*.py")
        if file.name != "__init__.py"
    ]
    await asyncio.gather(*tasks)


def generate_to_dict_method() -> str:
    return '''def to_dict(self) -> Dict[str, Any]:
        """Convert the dataclass instance to a dictionary."""
        return dataclasses.asdict(self)'''


def find_from_dict_method(tree: ast.AST) -> ast.ClassDef | None:
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if (
                    isinstance(item, ast.FunctionDef)
                    and item.name == "from_dict"
                    and any(
                        d.id == "classmethod"
                        for d in item.decorator_list
                        if isinstance(d, ast.Name)
                    )
                ):
                    return item
    return None


def adapt_from_dict_method(method_node: ast.ClassDef) -> str:
    """Convert the original from_dict method to use Optional and None instead of Union[Unset, ...] and UNSET."""
    source = ast.unparse(method_node)
    # Replace Union[Unset, with Optional[
    source = source.replace("Union[Unset, ", "Optional[")
    # Replace UNSET with None
    source = source.replace("UNSET", "None")
    # Replace all Unset instance checks using regex
    source = re.sub(r"isinstance\(([^,]+), Unset\)", r"\1 is None", source)
    # Fix imports to be relative
    source = source.replace("from ..models.", "from .")
    # Remove any remaining imports of Unset
    source = re.sub(r"from [\w.]+\s+import\s+.*?Unset.*?\n", "", source)
    # Remove additional_properties assignments
    lines = source.split("\n")
    filtered_lines = [line for line in lines if "additional_properties" not in line]
    return "\n".join(filtered_lines)


async def process_file(file: Path, output_dir: Path):
    async with aiofiles.open(file) as f:
        content = await f.read()

    tree = ast.parse(content)

    # Start with basic imports that should be in all files
    output_lines = [
        "from __future__ import annotations",
        "from typing import Dict, Any",
        "import dataclasses",
    ]

    if imports := get_imports_from_tree(tree):
        output_lines.extend(imports)
        output_lines.append("")

    # Process each node in the file
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            # Handle class definitions
            docstring = fix_docstring(ast.get_docstring(node))
            class_lines = ["\n@dataclasses.dataclass", f"class {node.name}:"]
            if docstring:
                class_lines.append(f'    """{docstring}"""')

            # Add fields
            for n in node.body:
                if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
                    name = n.target.id
                    if name == "additional_properties":
                        continue

                    annotation = ast.unparse(n.annotation)
                    annotation = annotation.replace("Union[Unset, ", "Optional[")
                    class_lines.append(f"    {name}: {annotation}")

            # Find and adapt the original from_dict method
            if original_from_dict := find_from_dict_method(node):
                adapted_from_dict = adapt_from_dict_method(original_from_dict)
                # Ensure proper indentation for the method
                lines = adapted_from_dict.split("\n")
                indented_lines = [
                    f"    {line}" if line.strip() else line for line in lines
                ]
                class_lines.append("\n" + "\n".join(indented_lines))

            # Add to_dict method with proper indentation
            to_dict_lines = generate_to_dict_method().split("\n")
            indented_to_dict = [
                f"    {line}" if line.strip() else line for line in to_dict_lines
            ]
            class_lines.append("\n" + "\n".join(indented_to_dict))

            output_lines.extend(class_lines)

        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            # Handle variable assignments and type definitions
            output_lines.append(ast.unparse(node))

        elif isinstance(node, ast.FunctionDef):
            # Handle function definitions
            output_lines.append("\n" + ast.unparse(node))

    # Write the output file
    output_file = output_dir / file.name
    async with aiofiles.open(output_file, "w") as f:
        await f.write("\n".join(output_lines))


if __name__ == "__main__":
    asyncio.run(generate_dataclasses(INPUT_DIR, OUTPUT_DIR))
