import json

config = json.load(open('config.json','r'))

host = config['host']
port = config['port']
username = config['username']
password = config['password']
prefix = config['prefix']
