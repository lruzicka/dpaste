#!/usr/bin/python3

import os
import argparse
import requests
import sys

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-f', '--file', default='empty', help='Input a file and paste the content.')
        self.parser.add_argument('-l', '--lexer', default='_text', help='Type of content - used for formatting.')
        self.parser.add_argument('-e', '--expire', default='hour', help='How long to keep the snippet online.')
        self.parser.add_argument('-c', '--content', default='empty', help='A content to be pasted to the webpage')

    def provide_arguments(self):
        args = self.parser.parse_args()
        return args

class Dpaster:
    def __init__(self, api, args):
        self.api = api    
        self.args = args
        self.expiry = None
        self.lexer = args.lexer 
        self.file = None
        self.content = None
        
    def convert_time(self):
        if self.args.expire == 'hour':
            self.expiry = 3600
        elif self.args.expire == 'day':
            self.expiry = 3600 * 24
        elif self.args.expire == 'week':
            self.expiry = 3600 * 24 * 7
        elif self.args.expire == 'month':
            self.expiry = 3600 * 24 * 30
        elif self.args.expire == 'never':
            self.expiry = 'never'
        else:
            self.expiry = 'onetime'
        return self.expiry

    def get_paste(self):
        # Get content to paste
        # If content taken from a file:
        if self.args.file != 'empty':
            with open(self.args.file) as infile:
                lines = infile.readlines()
            self.content = "".join(lines)
        
        # If provided on CLI
        elif self.args.content != 'empty':
            self.content = self.args.content
        
        # If provided by pipe
        elif sys.stdin:
            lines = [line for line in sys.stdin]
            self.content = "".join(lines)
        
        # If not provided at all
        else:
            self.content = "The user has not selected anything clever to paste, so we pasted this warning."
            print("You have not selected anything to paste")
        return self.content

    def prepare_paste(self):
        self.jsondata = {
            'format': 'url',
            'lexer': self.lexer,
            'expires': self.expiry,
            'content': self.content,
        }
        return self.jsondata
        

    def send_to_api(self):
        process = requests.post(self.api, data=self.jsondata)
        if process.status_code == 200:
            print(process.content.decode("utf-8"))
        else:
            print("Something went wrong, the content was not copied.")
            print(process.status_code)
        
def main():
    argparser = Parser()
    args = argparser.provide_arguments()

    application = Dpaster('https://dpaste.de/api/', args)
    
    # Calculate time in seconds to replace keywords.
    application.convert_time()

    application.get_paste()
        
    # Prepare data for API connection
    application.prepare_paste()
 
    # Connect with API
    application.send_to_api()


if __name__ == "__main__":
    main()
