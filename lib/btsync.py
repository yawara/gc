import json
import hashlib
import os
import sys

from btsyncapi import BtSyncApi

prefix = os.path.abspath(os.path.dirname(__file__)) + '/..'
try:
  cfg = json.load(open(prefix+'/config.json','r'))
except IOError:
  sys.exit('Not Found: config.json')
#if not os.path.exists(cfg['prefix']):
#  sys.exit('Not Found: cfg[prefix]')

class BTSync(BtSyncApi):
  def __init__(self,host=None,port=None,username=None,password=None,prefix=None):
    self.host = cfg['host'] if host is None else host
    self.port = cfg['port'] if port is None else port
    self.username = cfg['username'] if username is None else username
    self.password = cfg['password'] if password is None else password
    self.prefix = cfg['prefix'] if prefix is None else prefix
    BtSyncApi.__init__(self,self.host,self.port,self.username,self.password)

  def add_folder(self, folder, secret=None):
    if secret is None:
      secret = self.get_secrets()['read_write']
    return super(BTSync,self).add_folder(folder, secret)

  def register_secret(self, secret):
    dir_name = hashlib.sha256(secret).hexdigest()
    path = self.prefix + '/' + dir_name
    try:
      os.mkdir(path)
    except OSError:
      pass
    return self.add_folder(path,secret)

  def get_secrets(self,secret=None):
    return super(BTSync,self).get_secrets(secret,encryption=True)

  def get_encryption(self,secret):
    secrets = self.get_secrets(secret)
    if 'encryption' in secrets:
      return secrets['encryption']
    elif 'read_only' in secrets:
      return secrets['read_only']
    elif 'error' in secrets:
      raise Exception

  def validate_secret(self,secret):
    secrets = self.get_secrets(secret)
    return True if 'read_write' in secrets or 'read_only' in secrets or 'encryption' in secrets else False

  @staticmethod
  def validate_psuedo_secret(string):
    """
    Return True when the input string is a psuedo-valid secret.
    """
    return True if re.match('^[ABDEFR][0-9A-Z]{32,58}', string) else False
