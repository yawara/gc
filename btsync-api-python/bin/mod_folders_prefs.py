#!/usr/bin/env python
import btsync

b=btsync.BTSync()
ss = [ x['secret'] for x in b.get_folders() ]

for s in ss:
    print b.set_folder_prefs( s, { 'use_dht': 1, 'use_hosts': 1 } )
    print b.set_folder_hosts( s, [ 'btsync.asia:6881' ] )
