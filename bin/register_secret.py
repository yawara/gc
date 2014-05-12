#!/usr/bin/env python
from btsync import BTSync
import sys

secret = sys.argv[1]
b = BTSync()

print b.register_secret(secret)
