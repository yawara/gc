#!/usr/bin/env python
from btsync import BTSync

b = BTSync()

for folder in b.get_folders():
  print folder['secret']
