# README

This is a simple python wrapper around the BTSync API.

## Required
* Requests: HTTP for Humans http://docs.python-requests.org/en/latest/

## How to use
Edit the __config.json__ for your enviroment.

Set some enviroment variables.
```
PREFIX=$(cd $(dirname README.md); pwd)
export PYTHONPATH=$PREFIX/lib
export PATH=$PREFIX/bin:$PATH
```

Use and enjoy as follows!
```
from btsync import BTSync

b = BTSync()
print b.get_os()
print b.get_version()

```
