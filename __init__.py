import os
import subprocess
import cv2


class VideoBasler:

    def __init__(self, pipefile='test.pipe', target='test.tiff', use_opencv=False):
        module_root = os.path.dirname(__file__)
        self.pipefile = os.path.join(module_root, pipefile)
        if not os.path.exists(self.pipefile):
            os.mkfifo(self.pipefile)
        self.target = os.path.join(module_root, target)
        proc_path = './' if module_root is '' else module_root
        proc_exec = 'video_opencv' if use_opencv else 'video_basler'
        self.proc = subprocess.Popen(
            [os.path.join(proc_path, proc_exec), self.pipefile, self.target])

    def read(self):
        with open(self.pipefile, 'w') as pipe:
            pipe.write('request')
        with open(self.pipefile, 'r') as pipe:
            status = pipe.read().strip()
            if status == 'success':
                img = cv2.imread(self.target)
                if img is not None:
                    return True, img
            return False, None

    def close(self):
        with open(self.pipefile, 'w') as pipe:
            pipe.write('stop')
        os.remove(self.pipefile)
        os.remove(self.target)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--use-opencv', action='store_true')
    args = parser.parse_args()
    cap = VideoBasler(use_opencv=args.use_opencv)
    while True:
        status, img = cap.read()
        if status:
            cv2.imshow('main of VideoBasler', img)
            ch = 0xFF & cv2.waitKey(1)
            if ch == 27:
                cap.close()
                break
