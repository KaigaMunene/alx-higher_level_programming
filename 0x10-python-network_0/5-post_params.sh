#!/bin/bash
# Send POST request to passed URL and display body of response
curl -X POST -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
