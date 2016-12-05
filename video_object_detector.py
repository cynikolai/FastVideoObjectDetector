import sys, getopt
import numpy
import imageio
import optical_flow as of
import bounding_boxes as bb

# We will split the image into grid_size * grid_size regions within which we will detect objects.
grid_size = 10

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def proposal(image, previous_location, method):
	grayscale_image = rgb2gray(image)
	if(method == "N"):
		x = grayscale_image.shape[1]
		y = grayscale_image.shape[2]
		return 
	elif(method == "L"):
		# Return previous location of image
		return previous_location
	elif(method == "O"):
		# Return optical flow estimate of location of image
		return of.optical_flow_location_predictor(grayscale_image, previous_location)

def get_bounding_box_and_location(image, previous_location, method):



def main(argv):
   # Get command line arguments
   input_file = ''
   output_file = ''
   proposal_method = ''
   classifier_method = ''
   try:
      opts, args = getopt.getopt(argv,"i:o:p:c:",["ifile=","ofile="])
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-p", "--proposal"):
         proposal_method = arg
      elif opt in ("-c", "--classifier"):
         classifier_method = arg

    # Get input and output videos
    input_video = imageio.get_reader(input_file)
    output_video = imageio.get_writer(output_file)

    # initialize location and bounding box variables
    location = [0 ,0]
    bounding_box = [0, 0, 0, 0]

    # Get 
    location, bounding_box = location_prediction() 

    for i in range(get_length(input_video)):
      frame = input_video.get_data()
      location, bounding_box = 
    	



if __name__ == "__main__":
   main(sys.argv[1:])

