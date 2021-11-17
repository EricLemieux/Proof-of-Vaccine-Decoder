#!/usr/bin/env bash
# Decode a SMART QR proof of vaccine code

set -euo pipefail

source_file="${1-}"
if [[ -z "${source_file}" ]]; then
  echo "Must specify an input file" 1>&2
  exit 1
fi

zbarimg --raw --quiet "${source_file}" \
  | ./parse-shc.py \
  | ./parse-jwt.py \
  | jq
