import numpy as np
import cv2

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# Wrapper for OpenCV optical flow predictior
def optical_flow_location_predictor(image_1, image_2, x, y):

	lk_params = dict( winSize  = (15, 15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

	i1 = (rgb2gray(image_1)/256).astype('uint8')
	i2 = (rgb2gray(image_2)/256).astype('uint8')
	p1 = np.zeros((1,2))
	p2 = np.zeros((1,2))
	p1[0][1] = x
	p1[0][2] = y
	cv2.calcOpticalFlowPyrLK(i1, i2, p1, p2,  **lk_params)
	return p2[0][1], p2[0][2]