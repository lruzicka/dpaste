#!/usr/bin/python3

import os
import argparse
import requests
import sys

api = 'https://dpaste.de/api/'
lexer = '_text'
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', default='empty', help='Input a file and paste the content.')
parser.add_argument('-l', '--lexer', default='_text', help='Type of content - used for formatting.')
parser.add_argument('-e', '--expire', default='hour', help='How long to keep the snippet online.')
parser.add_argument('-c', '--content', default='empty', help='A content to be pasted to the webpage')

# Solve the variables first
args = parser.parse_args()
lexer = args.lexer

# Calculate time in seconds to replace keywords.
if args.expire == 'hour':
    expiry = 3600
elif args.expire == 'day':
    expiry = 3600 * 24
elif args.expire == 'week':
    expiry = 3600 * 24 * 7
elif args.expire == 'month':
    expiry = 3600 * 24 * 30
elif args.expire == 'never':
    expiry = 'never'
else:
    expiry = 'onetime'

# Get content to paste
# If content taken from a file:
if args.file != 'empty':
    with open(args.file) as infile:
        lines = infile.readlines()
    content = "".join(lines)

# If provided on CLI
elif args.content != 'empty':
    content = args.content

# If provided by pipe
elif sys.stdin:
    lines = [line for line in sys.stdin]
    content = "".join(lines)

# If not provided at all
else:
    content = "The user has not selected anything clever to paste, so we pasted this warning."
    expiry = 'onetime'
    print("You have not selected anything to paste")

# Prepare data for API connection
jsondata = {
    'format': 'url',
    'lexer': lexer,
    'expires': expiry,
    'content': content,
        }

# Connect with API
process = requests.post(api, data=jsondata)
if process.status_code == 200:
    print(process.content.decode("utf-8"))
else:
    print("Something went wrong, the content was not copied.")
    print(process.status_code)
