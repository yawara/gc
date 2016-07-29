# PyBasler

## Requirements

* Basler USB 3.0 cameras
* Pylon SDK 5
* opencv2
* Python2

## Usage
```
from pybasler import VideoBasler

cap = VideoBasler()
flag, img = cap
cv2.imshow('TEST', img)
cv2.waitKey(0)
```
