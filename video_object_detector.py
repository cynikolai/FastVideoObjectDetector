import sys, getopt

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



if __name__ == "__main__":
   main(sys.argv[1:])

