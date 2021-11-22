#!/usr/bin/env bash

set -euo pipefail

ls -1 Google-Sticker-Mashup-Research/stickers/ | grep -v '-' | cut -d. -f1 | tr _ '\n' | sort | uniq > emojis.txt

./generate_table.py > index.html
