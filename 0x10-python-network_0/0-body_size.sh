#!/bin/bash
# Sending a request and displaying content
response_byte=$(curl -s -o /dev/null -w '%{size_download}' "$1")
echo "${response_byte}"
