#!/bin/bash
# Display all http methods
curl -s -o /dev/null -w "%{http_code}" "$1"
