import os
import subprocess
import cv2


class VideoBasler:

    def __init__(self, feature_config="feature.pfs", use_opencv=False):

        module_root = os.path.dirname(__file__)
        pipefile = 'opencv.pipe' if use_opencv else 'basler.pipe'
        target = 'opencv.tiff' if use_opencv else 'basler.tiff'
        self.pipefile = os.path.join(module_root, pipefile)
        if not os.path.exists(self.pipefile):
            os.mkfifo(self.pipefile)
        self.target = os.path.join(module_root, target)
        proc_path = './' if module_root is '' else module_root
        proc_exec = 'video_opencv' if use_opencv else 'video_basler'
        if use_opencv:
            self.proc = subprocess.Popen(
                [os.path.join(proc_path, proc_exec), self.pipefile, self.target])
        else:
            self.proc = subprocess.Popen(
                [os.path.join(proc_path, proc_exec), self.pipefile, self.target, feature_config])

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
