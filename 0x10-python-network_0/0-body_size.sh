#!/bin/bash
# Sending a request and displaying content
echo "$(curl -s -o /dev/null -w '%{size_download}' "$1")"
