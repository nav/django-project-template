#!/usr/bin/env sh
set -eo pipefail

# This script reads config.json for the given app name and environment and
# makes the content available as environment variables.
#
# The application is expected to have the config file at `./ops/config.json`
# within the application folder.
#
# Sample config.json
# {
#  "application": {
#    "APP_NAME": "dashboard",
#    "NAMESPACE": "tarser",
#  },
#  "environment": {
#    "development": {
#      "RUNTIME_LEVEL": "development"
#    },
#    "production": {
#      "RUNTIME_LEVEL": "production",
#    }
#  }
# }

export APP_NAME={{ project_name|slugify }}

ENVIRONMENT=${1:-development}
CONFIG_PATH=${2:-./ops/config.json}

for s in $(cat ${CONFIG_PATH} \
    | jq '.environment.'${ENVIRONMENT} \
    | jq -r "to_entries|map(\"\(.key)=\(.value|tostring)\")|.[]"); do
    export $s
done

for s in $(cat ${CONFIG_PATH} \
    | jq '.application' \
    | jq -r "to_entries|map(\"\(.key)=\(.value|tostring)\")|.[]"); do
    export $s
done

DIR="$(cd "$(dirname "$0")" >/dev/null 2>&1 && pwd)"
