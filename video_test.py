# Dependencies
import sys, getopt
import numpy
import imageio
from PIL import Image, ImageDraw
import cv2
import time

# Helper scripts
import optical_flow as of
import bounding_boxes as bb
import region_proposals as rp
import classify_image as cf

TEST_LENGTH_1 = 53
TEST_LENGTH_2 = 250

# Object to search for
search_object = 'cat'

# Number of highest priority objects to check
num_priority = 3

# Number of frames to check
num_frames_to_detect = 10

from Queue import PriorityQueue

# Priority queue structure to order 
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item

# Image display helper functions
def draw_image(image_name, bounding_box, classification, score):
  im = Image.open(image_name)
  draw = ImageDraw.Draw(im)
  draw.rectangle(bounding_box)
  draw.text([15,15], "Classification : " + classification)
  draw.text([15,30], "Certainty : " + str(score))
  im.show()

def get_frame(test, frame_num):
    if(frame_num > 99):
      frame_str = '0' + str(frame_num)
    elif(frame_num > 9):
      frame_str = '00' + str(frame_num)
    else:
      frame_str = '000' + str(frame_num)
    frame_name = 'frame' + frame_str + '.jpg'
    if(test == 1):
      frame_path = 'test/test_cats_1/'
    if(test == 2):
      frame_path = 'test/test_cats_2/'
    return frame_path+frame_name

def image_slice(image, bounding_box):
  x_0 = bounding_box[0]
  x_1 = bounding_box[2]
  y_0 = bounding_box[1]
  y_1 = bounding_box[2]
  return image[x_0:x_1,y_0:y_1]

# RCNN without using temporal information
def object_locate(test, frame):
  image_name = get_frame(test,frame)
  img = cv2.imread(image_name)
  region_proposals = rp.generate_region_proposals(image_name)
  max_score = 0
  max_score_abs = 0
  bounding_box = [0, 0, 0, 0]
  classification = ''
  print "Number of proposals: " + str(len(region_proposals))
  for region in region_proposals:
      print "Checking Another Region Proposal"
      bounding_box_test = rp.bounding_box_from_region(region)
      image_bit = image_slice(img, bounding_box_test)
      cv2.imwrite('convolute.jpg', image_bit)
      convolve = cv2.imread('convolute.jpg')
      if convolve is not None:
        width, height, channels = convolve.shape
        area = width * height
        human_string, score_new = cf.classify('convolute.jpg')
      else:
        continue
      score = score_new / area
      if(score > max_score):
          bounding_box = bounding_box_test
          max_score = score
          max_score_abs = score_new
          classification = human_string
      if(human_string.find(search_object) != -1):
          classification = human_string
  return bounding_box, max_score_abs, classification

# RCNN with using temporal information
def object_locate_prev_frame(test, frame, imscale_prev):
  image_name = get_frame(test,frame)
  img = cv2.imread(image_name)
  region_proposals = rp.generate_region_proposals(image_name)
  max_score = 0
  max_score_abs = 0
  bounding_box = [0, 0, 0, 0]
  classification = ''
  print "Number of proposals: " + str(len(region_proposals))
  # Priority queue for region proposals
  queue = MyPriorityQueue()
  for region in region_proposals:
      bounding_box_test = rp.bounding_box_from_region(region)
      imscale_test = bb.bounding_box_to_imscale(bounding_box_test)
      # Get proposal priority
      priority = bb.imscale_priority(imscale_prev, imscale_test)
      queue.put(region, -priority)
  for i in range(num_priority):
      region = queue.get()
      bounding_box_test = rp.bounding_box_from_region(region)
      print "Checking Another Region Proposal"
      image_bit = image_slice(img, bounding_box_test)
      cv2.imwrite('convolute.jpg', image_bit)
      convolve = cv2.imread('convolute.jpg')
      if convolve is not None:
        width, height, channels = convolve.shape
        area = width * height
        human_string, score_new = cf.classify('convolute.jpg')
      else:
        continue
      score = score_new / area
      if(score > max_score):
          bounding_box = bounding_box_test
          max_score = score
          max_score_abs = score_new
          classification = human_string
      if(human_string.find(search_object) != -1):
          classification = human_string
  return bounding_box, max_score_abs, classification


def main(argv):
  print "Video Object Detector Test"
  start_time = time.time()
  # Two tests: test 1 and test 2
  test = 1

  if(test == 1):
    test_length = TEST_LENGTH_1
  if(test == 2):
    test_length = TEST_LENGTH_2
  
  # Find object in first frame using RCNN
  bounding_box, max_score, classification = object_locate(test, 1) 
  draw_image(get_frame(test,1), bounding_box, classification, max_score)

  # Estimate new imscale with object flow
  imscale = bb.bounding_box_to_imscale(bounding_box)
  x = imscale[0]
  y = imscale[1]
  image_1 = cv2.imread(get_frame(test,1), 0)
  image_2 = cv2.imread(get_frame(test,2), 0)
  x_new, y_new = of.optical_flow_location_predictor(image_1, image_2, x,y)
  imscale_prev = bb.predict_imscale(x_new, y_new, imscale)

  # Find object in frames 2-10 using fast video detection algorithm
  for i in range(2, num_frames_to_detect):
    bounding_box, max_score, classification = object_locate_prev_frame(test, i, imscale_prev)
    imscale = bb.bounding_box_to_imscale(bounding_box)
    x = imscale[0]
    y = imscale[1]
    image_1 = cv2.imread(get_frame(test,i), 0)
    image_2 = cv2.imread(get_frame(test,i+1), 0)
    x_new, y_new = of.optical_flow_location_predictor(image_1, image_2, x,y)
    imscale_prev = bb.predict_imscale(x_new, y_new, imscale)
    draw_image(get_frame(test,i), bounding_box, classification, max_score)

    print("--- %s seconds per image---" % ((time.time() - start_time)/num_frames_to_detect))

if __name__ == "__main__":
   main(sys.argv[1:])