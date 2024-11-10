import ast
import asyncio
from pathlib import Path

import aiofiles

SCRIPT_DIR = Path(__file__).parent
PKG_NAME = "oanda_v20_client"
INPUT_DIR = SCRIPT_DIR / PKG_NAME / "src" / PKG_NAME / "models"
OUTPUT_DIR = SCRIPT_DIR / PKG_NAME / "src" / PKG_NAME / "dataclasses"


def get_imports_from_tree(tree: ast.AST) -> list[str]:
    imports = set()  # Changed to set to prevent duplicates
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module:
                names = ", ".join(n.name for n in node.names)
                if "models." in node.module:
                    # Use relative imports instead of pydantic
                    imports.add(f"from .{node.module.split('.')[-1]} import {names}")
                else:
                    imports.add(f"from {node.module} import {names}")
        elif isinstance(node, ast.Import):
            for name in node.names:
                imports.add(f"import {name.name}")
    return sorted(imports)  # Convert back to sorted list


async def generate_pydantic_models(input_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    await generate_unset_module(output_dir)
    (output_dir / "__init__.py").touch()

    tasks = [
        process_file(file, output_dir)
        for file in input_dir.rglob("*.py")
        if file.name != "__init__.py"
    ]
    await asyncio.gather(*tasks)


async def generate_unset_module(output_dir: Path):
    content = "from typing import Literal\n\nclass Unset:\n    def __bool__(self) -> Literal[False]:\n        return False\n\nUNSET: Unset = Unset()"
    async with aiofiles.open(output_dir / "types.py", "w") as f:
        await f.write(content)


def generate_to_dict_method() -> str:
    return '''
    def to_dict(self) -> Dict[str, Any]:
        """Convert the dataclass instance to a dictionary."""
        return dataclasses.asdict(self)'''


def generate_from_dict_method(class_name: str) -> str:
    return f'''
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "{class_name}":
        """Create a new instance from a dictionary."""
        return from_dict(data_class=cls, data=data)'''


async def process_file(file: Path, output_dir: Path):
    async with aiofiles.open(file) as f:
        content = await f.read()

    tree = ast.parse(content)

    # Start with basic imports that should be in all files
    output_lines = [
        "from __future__ import annotations",
        "from typing import Dict, Any",
        "import dataclasses",
        "from dacite import from_dict",
    ]

    if imports := get_imports_from_tree(tree):
        output_lines.extend(imports)
        output_lines.append("")

    # Process each node in the file
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            # Handle class definitions
            docstring = ast.get_docstring(node)
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
                    default = (
                        " = UNSET"
                        if not n.value
                        or (isinstance(n.value, ast.Name) and n.value.id == "UNSET")
                        else f" = {ast.unparse(n.value)}"
                    )

                    class_lines.append(f"    {name}: {annotation}{default}")

            class_lines.extend(
                (
                    generate_to_dict_method(),
                    generate_from_dict_method(node.name),
                )
            )
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
    asyncio.run(generate_pydantic_models(INPUT_DIR, OUTPUT_DIR))
