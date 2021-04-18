#!/usr/bin/env python3
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('videos/1_1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
delay_ms = int(round((1/fps) * 1000))
player = MediaPlayer('videos/1_1.mp4')
window_name = "window"
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video  file")
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


def play_cutscene_1_1():
    while cap.isOpened():
    # Capture frame-by-frame
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()
        if not ret:
            print("end of the video")
            break

        if cv2.waitKey(26) & 0xFF == ord('s'):
            break
        cv2.imshow(window_name, frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    # When everything done, release
    # the video capture object
    player.close_player()
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()
