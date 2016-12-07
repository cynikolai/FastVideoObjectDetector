# Fast Video Object Detector

![Alt text](cat_demo.png?raw=true "A frame detected by the algorithm")

Final project for EECS 442 Fall 2016 at the University of Michigan.

This repository, given an input mp4 video, adapts the RCNN method of object detection in images to more quickly work in videos by using the temporal information available in natural videos. 

This is a proof-of concept for using temporal information in object detection in videos, and is not a state-of-the-art algorithm.

To run a test with the video data in the test folder, run python video_test.py.

**Requirements**

OpenCV: http://opencv.org/downloads.html

Tensorflow: https://github.com/tensorflow/tensorflow

Selective Search: https://github.com/AlpacaDB/selectivesearch

**Usage**: video_object_detector.py -i \<input_file> -o \<output_file> -p \<proposal_method> -c \<classification_method>

**input file**: a mp4 file containing the input video

**output file**: a mp4 file containing the output video with bounding boxes drawn

**proposal method**: the method by which the object detector estimates object location in subsequent frames. Can be "L" for local, "O" for optical flow, or "N" for no prediction.

**classification method**: specifies the convolutional network used to check for objects within a given proposal.

You can download videos from youtube to use with the fast video object detector with the script youtube_object_detector.py (requires pytube).

**Usage**: youtube_object_detector.py -l \<input_link> -r \<resolution>

This creates two copy videos in the current directory vid_original.mp4 and vid_bounded.mp4.

# Citations

[1] J. R. R. Uijlings et al., Selective Search for Object Recognition, IJCV, 2013 

[2] R. Girshick, J. Donahue, T. Darrell, and J. Malik, “Rich feature hierarchies for accurate object detection and semantic segmentation,” in IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2014

[3] Lucas, Bruce D., and Takeo Kanade. "An iterative image registration technique with an application to stereo vision." IJCAI. Vol. 81. No. 1. 1981.

[4] Horn, Berthold KP, and Brian G. Schunck. "Determining optical flow." Artificial intelligence 17.1-3 (1981): 185-203.
