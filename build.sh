#!/usr/bin/env bash
set -e # Exit on error

# Constants
VENV_DIR=".venv"
CLIENT_DIR="oanda_v20_client"
MAX_RETRIES=5
RETRY_DELAY=2

# Function to wait for directory
wait_for_directory() {
    local dir=$1
    local retries=0

    while [ ! -d "$dir" ] && [ $retries -lt $MAX_RETRIES ]; do
        echo "Waiting for directory $dir to be created..."
        sleep $RETRY_DELAY
        retries=$((retries + 1))
    done

    if [ ! -d "$dir" ]; then
        echo "Error: Directory $dir was not created after $MAX_RETRIES attempts"
        exit 1
    fi
}

# Function to display help message
show_help() {
    echo "Usage: ./build.sh [command]"
    echo ""
    echo "Available commands:"
    echo "  cleanup       - Clean all generated files and dependencies"
    echo "  install_deps  - Install dependencies"
    echo "  convert_api   - Convert Oanda Swagger API to OpenAPI"
    echo "  clean        - Remove generated client code and build artifacts"
    echo "  generate     - Generate Python client from OpenAPI specification"
    echo "  bump_version - Bump minor version in pyproject.toml"
    echo "  build        - Build the package using UV"
    echo "  publish      - Publish package to PyPI"
    echo "  help         - Show this help message"
}

# Cleanup function
cleanup() {
    echo "Performing deep cleanup..."
    rm -rf "${VENV_DIR}"
    rm -rf node_modules
    rm -rf "${CLIENT_DIR}"
    rm -rf openapi.yaml
    rm -f pnpm-lock.yaml
    rm -f uv.lock
    echo "Cleanup completed successfully!"
}

# Install dependencies
install_deps() {
    echo "Installing dependencies..."
    uv lock --upgrade
    uv sync
    pnpm install
}

# Convert API
convert_api() {
    echo "Converting Oanda Swagger API to OpenAPI..."
    install_deps
    pnpm run convert
}

# Clean artifacts
clean() {
    echo "Cleaning up old artifacts..."
    rm -rf "${CLIENT_DIR}"
    rm -rf ./*.egg-info
    rm -rf ./*/dist
    rm -rf ./*/__pycache__
}

# Generate Python client
generate() {
    echo "Generating Python client from OpenAPI specification..."
    clean
    convert_api
    chmod +x ./gen.sh
    ./gen.sh

    # Wait for directory to be created
    wait_for_directory "${CLIENT_DIR}"
}

# Bump version
bump_version() {
    echo "Bumping minor version..."
    VERSION=$(awk -F'"' '/version/ {print $2}' pyproject.toml)
    MAJOR="$(echo "$VERSION" | cut -d. -f1)"
    MINOR="$(echo "$VERSION" | cut -d. -f2)"
    PATCH="$(echo "$VERSION" | cut -d. -f3)"
    NEW_MINOR=$((MINOR + 1))
    NEW_VERSION="${MAJOR}.${NEW_MINOR}.${PATCH}"

    # Cross-platform sed command
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s/version = \"${VERSION}\"/version = \"${NEW_VERSION}\"/" pyproject.toml
    else
        # Linux and other platforms
        sed -i "s/version = \"${VERSION}\"/version = \"${NEW_VERSION}\"/" pyproject.toml
    fi

    echo "Version bumped to $NEW_VERSION"
}

# Build package
build() {
    generate
    wait_for_directory "${CLIENT_DIR}"

    cd "${CLIENT_DIR}" || exit 1

    # Create src directory and package directory
    mkdir -p "src/${CLIENT_DIR}"

    # Move all Python files to the correct location
    mv api "src/${CLIENT_DIR}/"
    mv client.py "src/${CLIENT_DIR}/"
    mv errors.py "src/${CLIENT_DIR}/"
    mv models "src/${CLIENT_DIR}/"
    mv types.py "src/${CLIENT_DIR}/"
    mv __init__.py "src/${CLIENT_DIR}/"

    # Create pyproject.toml and README.md in the root
    cat >README.md <<'EOF'
# OANDA v20 Python Client

A Python client library for the OANDA v20 REST API.

## Installation

```bash
pip install oanda-v20-client
```

## Usage

```python
from oanda_v20_client import Client

# Initialize the client
client = Client(base_url="your_base_url", token="your_token")
```
EOF

    cat >pyproject.toml <<'EOF'
[project]
name = "oanda-v20-client"
version = "0.0.1"
description = "A client library for accessing OANDA v20 REST API"
authors = [{ name = "Takin Profit LLC", email = "takinprofit@gmail.com"}]
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT License"}
dependencies = [
    "httpx>=0.20.0,<0.28.0",
    "attrs>=21.3.0",
    "python-dateutil>=2.8.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build]
packages = ["src/oanda_v20_client"]
EOF

    bump_version
    rm -rf dist
    uv lock --upgrade
    uv sync
    uv build
}
# Publish package
publish() {
    wait_for_directory "${CLIENT_DIR}"
    cd "${CLIENT_DIR}" || exit 1
    if [ -z "$PYPI_TOKEN" ]; then
        echo "Error: PYPI_TOKEN environment variable is required"
        exit 1
    fi
    uv publish --token "$PYPI_TOKEN"
}

# Main function to handle command routing
main() {
    case $1 in
    "cleanup")
        cleanup
        ;;
    "install_deps")
        install_deps
        ;;
    "convert_api")
        convert_api
        ;;
    "clean")
        clean
        ;;
    "generate")
        generate
        ;;
    "bump_version")
        wait_for_directory "${CLIENT_DIR}"
        cd "${CLIENT_DIR}" || exit 1
        bump_version
        ;;
    "build")
        build
        ;;
    "publish")
        build
        publish
        ;;
    "help" | "--help" | "-h" | "")
        show_help
        ;;
    *)
        echo "Unknown command: $1"
        echo "Use './build.sh help' to see available commands"
        exit 1
        ;;
    esac
}

# Execute main function with all arguments
main "$@"
