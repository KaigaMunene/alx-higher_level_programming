#!/bin/bash
# Send a GET request to URL and display the status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
