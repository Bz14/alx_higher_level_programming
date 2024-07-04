#!/bin/bash
# Sending a request and displaying content
curl -s "$1" | wc -c
