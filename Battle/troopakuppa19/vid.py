#!/usr/bin/env python3
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer




def play_cutscene_1_1():
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture('videos/1_1.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    player = MediaPlayer('videos/1_1.mp4')
    window_name = "window"
    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video  file")
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
    # Capture frame-by-frame
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()
        if not ret:
            print("end of the video")
            break

        if cv2.waitKey(28) & 0xFF == ord('s'):
            break
        cv2.imshow(window_name, frame)
        #if val != 'eof' and audio_frame is not None:
           # pass
            #audio
            #img, t = audio_frame
            #print(t)
    # When everything done, release
    # the video capture object
    player.close_player()
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()
