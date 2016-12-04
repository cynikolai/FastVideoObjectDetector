import sys, getopt
import numpy
import imageio
import optical_flow as of

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

def get_bounding_box(image, previous_location, method):

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
    input_image = imageio.get_reader(input_file)
    output_image = imageio.get_writer(output_file)

    # Get 
    prediction = location_prediction() 

    for i in range(get_length(input_image)):
    	



if __name__ == "__main__":
   main(sys.argv[1:])

