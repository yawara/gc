#!/usr/bin/env python
from btsync import BTSync

b = BTSync()

print 'listen : {0}:{1}'.format(b.host,b.port)
print b.get_os()
print b.get_version()
print b.get_speed()
