import json
import hashlib
import os

from btsyncapi import BtSyncApi

prefix = os.path.abspath(os.path.dirname(__file__)) + '/..'
cfg = json.load(open(prefix+'/config.json','r'))

class BTSync(BtSyncApi):
  def __init__(self,host=None,port=None,username=None,password=None,prefix=None):
    self.host = cfg['host'] if host is None else host
    self.port = cfg['port'] if port is None else port
    self.username = cfg['username'] if username is None else username
    self.password = cfg['password'] if password is None else password
    self.prefix = cfg['prefix'] if prefix is None else prefix
    BtSyncApi.__init__(self,self.host,self.port,self.username,self.password)

  def register_secret(self, secret):
    dir_name = hashlib.sha256(secret).hexdigest()
    path = self.prefix + '/' + dir_name

    try:
      os.mkdir(path)
    except OSError:
      pass

    return self.add_folder(path,secret)
