#!/bin/bash
# Display all http methods
curl -s -H "Content-Type: application/json" -d "$(cat $2)" "$1"
