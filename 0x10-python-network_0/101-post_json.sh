#!/bin/bash
# Send a Post equest to URL and display the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
