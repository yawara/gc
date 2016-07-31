#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import chainer
import cv2 as cv
import numpy as np

from forward import CLASSES, PIXEL_MEANS, get_model, img_preprocessing, draw_result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nms_thresh', type=float, default=0.3)
    parser.add_argument('--conf', type=float, default=0.8)
    parser.add_argument('--gpu', type=int, default=-1)
    args = parser.parse_args()

    xp = chainer.cuda.cupy if chainer.cuda.available and args.gpu >= 0 else np
    model = get_model(gpu=args.gpu)
    if chainer.cuda.available and args.gpu >= 0:
        model.to_gpu(args.gpu)

    cap = cv.VideoCapture()
    while True:
        status, orig_image = cap.read()
        if not status:
            continue

        img, im_scale = img_preprocessing(orig_image, PIXEL_MEANS)
        img = np.expand_dims(img, axis=0)
        if args.gpu >= 0:
            img = to_gpu(img, device=args.gpu)
        img = chainer.Variable(img, volatile=True)
        h, w = img.data.shape[2:]
        cls_score, bbox_pred = model(img, np.array([[h, w, im_scale]]))
        cls_score = cls_score.data

        if args.gpu >= 0:
            cls_score = chainer.cuda.cupy.asnumpy(cls_score)
            bbox_pred = chainer.cuda.cupy.asnumpy(bbox_pred)
        result = draw_result(orig_image, im_scale, cls_score, bbox_pred,
                             args.nms_thresh, args.conf)
        cv.imshow('Faster RCNN', result)
        if 0xFF & cv2.waitKey(1) == 27:
            break

    cv.destroyAllWindows()
