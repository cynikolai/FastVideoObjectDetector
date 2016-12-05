# FastVideoObjectDetector

This repository, given an input mp4 video, adapts the RCNN method of object detection in images to quickly work in videos by using the temporal information available in natural videos.

**Requirements**

OpenCV:
Tensorflow:
EdgeBoxes:

**Usage**: video_object_detector.py -i \<input_file> -o \<output_file> -p \<proposal_method> -c \<classification_method>

**input file**: a mp4 file containing the input video

**output file**: a mp4 file containing the output video with bounding boxes drawn

**proposal method**: the method by which the object detector estimates object location in subsequent frames. Can be "L" for local, "O" for optical flow, or "N" for no prediction.

**classification method**: specifies the convolutional network used to check for objects within a given proposal.
