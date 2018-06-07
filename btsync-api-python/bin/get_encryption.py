#!/usr/bin/env python
import sys
from btsync import BTSync

secret = sys.argv[1]
b = BTSync()

print b.get_encryption(secret)
