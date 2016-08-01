from pybasler import VideoBasler
import cv2

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--use-opencv', action='store_true')
#parser.add_argument('--exposure-time', default=100000)
parser.add_argument('--feature-config',
                    default=os.path.join(os.path.dirname(__file__), 'feature.pfs'))
parser.add_argument('--N', type=float, default=3.5)
args = parser.parse_args()
cap = VideoBasler(feature_config=args.feature_config, use_opencv=args.use_opencv)
while True:
    status, img = cap.read()
    if status:
        height, width = img.shape[:2]
        vis = cv2.resize(img, (int(width / args.N), int(height / args.N)))
        cv2.imshow('main of VideoBasler', vis)
        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            cap.close()
            break
