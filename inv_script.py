#!/usr/bin/python
from argparse import ArgumentParser
import json
import requests
import time

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--list', dest='list_instances', action='store_true', default=True,
                        help='List instances (default: True)')
    parser.add_argument('--host', dest='requested_host', help='Get all the variables about a specific instance')
    return parser.parse_args()

def main():
  res=requests.get('https://raw.githubusercontent.com/fosterseth/playbooks/master/inv.json')
  data=res.json()
  print(json.dumps(data, sort_keys=True, indent=2))
if __name__ == '__main__':
  main()
