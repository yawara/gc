#!/usr/bin/env python
from btsync import BTSync
import sys

secrets_file = sys.argv[1]
b = BTSync()

for secretWithN in open(secrets_file,'r'):
  print b.register_secret(secretWithN.strip())
