from btsyncapi import BtSyncApi
import config
import hashlib,os

class BTSync(BtSyncApi):
  def __init__(self,host=None,port=None,username=None,password=None,prefix=None):
    self.host = config.host if host is None else host
    self.port = config.port if port is None else port
    self.username = config.username if username is None else username
    self.password = config.password if password is None else password
    self.prefix = config.prefix if prefix is None else prefix
    BtSyncApi.__init__(self,self.host,self.port,self.username,self.password)

  def register_secret(self, secret):
    dir_name = hashlib.sha256(secret).hexdigest()
    path = self.prefix + '/' + dir_name

    try:
      os.mkdir(path)
    except OSError:
      pass

    return self.add_folder(path,secret)
