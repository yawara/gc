#!/usr/bin/env python
import sys
import os
import time

from btsync import BTSync

DB_PREFIX='/Users/ywr/BTSync/db/ywr/'
RESCAN_INTERVAL=5

if not os.path.exists(DB_PREFIX):
    sys.exit("Not Found: " + DB_PREFIX)

b = BTSync()

while True:
    print 'sleep for', RESCAN_INTERVAL, 'seconds...'
    time.sleep(RESCAN_INTERVAL)
    secrets = os.listdir(DB_PREFIX)
    if secrets == []:
        print 'secrets is empty, continue'
        continue
    for secret in secrets:
        if b.validate_secret(secret):
            print 'valid secret:', secret
            print 'try to register', secret
            msg = b.register_secret(secret)
            print msg
            if msg['error'] in {0,200}:
                try:
                    os.rmdir(DB_PREFIX+secret)
                    print 'successfully removed from db'
                except OSError:
                    print 'failed to remove from db'
            else:
                pass
        else:
            print 'invalid secret:', secret
            try:
                os.rmdir(DB_PREFIX+secret)
                print 'successfully removed from db'
            except OSError:
                print 'failed to remove from db'
