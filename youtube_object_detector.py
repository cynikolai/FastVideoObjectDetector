from pytube import YouTube
import sys, getopt

def main(argv):
   # Get command line arguments
   input_link = ''
   input_resolution = ''
   
   
   opts, args = getopt.getopt(argv,"l:r:",["link=","res="])
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -l <link>'
      elif opt in ("-l", "--link"):
         input_link = arg
      elif opt in ("-r", "--res"):
         input_resolution = arg

   yt = YouTube(input_link)
   yt.set_filename('vid_original')
   video = yt.get('mp4', input_resolution)
   video.download('')

   yt = YouTube(input_link)
   yt.set_filename('vid_bounded')
   video = yt.get('mp4', input_resolution)
   video.download('')

if __name__ == "__main__":
   main(sys.argv[1:])