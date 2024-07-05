#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

import requests
import sys

url = 'http://0.0.0.0:5000/search_user'

# Check if a letter argument is provided, set q="" if not
letter = sys.argv[1] if len(sys.argv) > 1 else ""

# Prepare the data for the POST request
data = {'q': letter}

# Send the POST request
response = requests.post(url, data=data)

try:
    # Try to parse the JSON response
    result = response.json()

    # Check if the JSON response is empty
    if result:
        print(f"[{result.get('id')}] {result.get('name')}")
    else:
        print("No result")
except ValueError:
    # Handle JSON decoding error
    print("Not a valid JSON")
