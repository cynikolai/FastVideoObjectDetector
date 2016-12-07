import numpy as np

# Imscale: center coordinates of image location, followed by half width and height of bounding box
# Bounding box - bottom left and top right coordinates of bounding box

# For a predicted imscale, evaluate the priority of a region proposal
def imscale_priority(imscale_predicted, imscale):
	delta_vector = abs(np.asarray(imscale_predicted) - np.asarray(imscale))
	return 1 / np.dot(delta_vector, delta_vector)


# For a given optical flow, predict an imscale from the imscale in the previous frame
def predict_imscale(v_x, v_y, imscale):
	imscale_predict = imscale
	imscale_predict[0] += v_x
	imscale_predict[1] += v_y
	return imscale_predict


# Return a bounding box for a given imscale
def bounding_box_to_imscale(bounding_box):
	x_c =  (bounding_box[0] + bounding_box[2]) / 2
	y_c =  (bounding_box[1] + bounding_box[3]) / 2
	x_r =  (bounding_box[2] - bounding_box[0]) / 2
	y_r =  (bounding_box[3] - bounding_box[1]) / 2
	return [x_c, y_c, x_r, y_r]


# Return an imscale for a given bounding box
def imscale_to_bounding_box(imscale):
	x_1 = imscale[0] + imscale[2]
	y_1 = imscale[1] + imscale[3]
	x_0 = imscale[0] - imscale[2]
	y_0 = imscale[1] - imscale[3]
	return [x_0, y_0, x_1, y_1]


# Get the area of a bounding box
def area(bounding_box):
	x = bounding_box[2] - bounding_box[0]
	y = bounding_box[3] - bounding_box[1]
	return x * y

# Get the intersection over union
def IOU(bounding_box, ground_truth_bounding_box):
	area_1 = area(bounding_box)
	area_2 = area(ground_truth_bounding_box)
	# no overlapping area
	if(bounding_box[0] > ground_truth_bounding_box[2]):
		return false
	if(bounding_box[2] < ground_truth_bounding_box[0]):
		return false
	if(bounding_box[1] > ground_truth_bounding_box[3]):
		return false
	if(bounding_box[3] < ground_truth_bounding_box[1]):
		return false
	# Positive overlapping area
	ex_0 = max(bounding_box[0], ground_truth_bounding_box[0])
	ex_1 = max(bounding_box[1], ground_truth_bounding_box[1])
	ex_2 = min(bounding_box[2], ground_truth_bounding_box[2])
	ex_3 = min(bounding_box[3], ground_truth_bounding_box[3])
	effective_union = [ex_0, ex_1, ex_2, ex_3]
	area_c = area(effective_union)
	union = area_1 + area_2 - area_c
	intersection = area_c
	return (intersection/union)
