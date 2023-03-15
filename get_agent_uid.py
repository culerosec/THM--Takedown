#!/usr/env/python3

import requests
import json
import base64
import sys


def get_uid():

    url = "http://"+sys.argv[1]
    endpoint = "/api/agents"
    headers = {
	    "Content-Type" : "application/json",
         "User-Agent" : "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5"
        }
    r = requests.get(url+endpoint, headers = headers)
    print(r.text)
    data = (r.json())

def main():
    get_uid()  
   

if __name__ == '__main__':
    main()