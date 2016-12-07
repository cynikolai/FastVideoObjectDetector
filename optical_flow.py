import numpy as np
import cv2

# Wrapper for OpenCV optical flow predictior
def optical_flow_location_predictor(image_1, image_2, x, y):

	lk_params = dict( winSize  = (15, 15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
	feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
	p0 = cv2.goodFeaturesToTrack(image_1, mask = None, **feature_params)

	p0[0][0][0] = 1. * x
	p0[0][0][1] = 1. * y

	# OpenCV function for calculation of optical flow
	p2, st, err = cv2.calcOpticalFlowPyrLK(image_1, image_2, p0,  **lk_params)
	return int(p2[0][0][0]), int(p2[0][0][1])