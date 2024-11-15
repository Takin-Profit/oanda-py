#!/usr/bin/env bash
# Copyright 2024 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

set -e # Exit on error

open_api_client="./.venv/bin/openapi-python-client"
ruff="./.venv/bin/ruff"
oanda_api="./openapi.yaml"
config="./openapi-client-config.yml"

# Create config file if it doesn't exist
if [ ! -f "$config" ]; then
    echo "Creating config file..."
    cat >"$config" <<EOF
project_name_override: oanda-v20-client
package_name_override: oanda_v20_client
post_hooks:
  - "$ruff check . --fix"
  - "$ruff format ."
EOF
fi

if [ ! -f "$open_api_client" ]; then
    echo "Error: openapi-python-client not found at $open_api_client"
    echo "Please ensure it's installed in your virtual environment"
    exit 1
fi

# Run conversion script and wait for it to complete
echo "Converting Swagger to OpenAPI 3.0..."
node convert.js
if [ ! -f "$oanda_api" ]; then
    echo "Error: OpenAPI file not generated at $oanda_api"
    exit 1
fi

# Generate the client
echo "Generating Python client from OpenAPI specification..."
if "$open_api_client" generate --path "$oanda_api" --config "$config" --overwrite --meta none; then
    echo "Successfully generated Python client!"
else
    echo "Error: Failed to generate Python client"
    exit 1
fi
