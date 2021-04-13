#!/usr/bin/env python3
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('videos/1_1.mp4')
player = MediaPlayer('videos/1_1.mp4')
window_name = "window"
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video  file")
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


def play_cutscene_1_1():
    while True:
    # Capture frame-by-frame
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()
        if ret == True:
            # Display the resulting frame
            cv2.imshow(window_name, frame)
            # Press Q on keyboard to  exit
            if cv2.waitKey(28) & 0xFF == ord('q'):
                break
            if val != 'eof' and audio_frame is not None:
                #audio
                img, t = audio_frame
            # Break the loop
        else:
            break
    # When everything done, release
    # the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()
