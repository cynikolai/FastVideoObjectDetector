import skimage.data
import selectivesearch
import cv2

# Generate region proposals for an input image
def generate_region_proposals(image_name):
	image = cv2.imread(image_name,-1)
	img_lbl, regions = selectivesearch.selective_search(image, scale=500, sigma=0.8, min_size=2000)
	candidates = set()
	for r in regions:
        # excluding same rectangle (with different segments)
		if r['rect'] in candidates:
			continue
        # excluding regions smaller than 2000 pixels
		if r['size'] < 2000:
			continue
        # distorted rects
		x, y, w, h = r['rect']
		if w / h > 1.2 or h / w > 1.2:
			continue
		candidates.add(r['rect'])
	return candidates

# Extract bounding box coordinates
def bounding_box_from_region(region):
	return [region[0], region[1], region[0]+region[2], region[1]+region[3]]

