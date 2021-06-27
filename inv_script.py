#!/usr/bin/python

import json
import requests

def main():
  res=requests.get('https://raw.githubusercontent.com/fosterseth/playbooks/master/inv.json')
  data=res.json()
  print json.dumps(data, sort_keys=True, indent=2)
if __name__ == '__main__':
  main()
