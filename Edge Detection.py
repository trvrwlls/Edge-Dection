import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



def do_canny(frame):

    # Converts frame to grayscale because we only need the luminance channel for detecting edges - less computationally expensive
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

    # Applies a 5x5 gaussian blur with deviation of 0 to frame - not mandatory since Canny will do this for us
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    # Applies Canny edge detector with minVal of 50 and maxVal of 150
    canny = cv.Canny(blur, 50, 150)
    return canny
    

    
# The video feed is read in as a VideoCapture object
cap = cv.VideoCapture(0)
while (cap.isOpened()):

    # ret = a boolean return value from getting the frame, frame = the current frame being projected in the video
    ret, frame = cap.read()

    if ret:

        cv.imshow('Original Video', frame)

        canny = do_canny(frame)
        cv.imshow('Canny', canny)
        print(canny)

    

    # Frames are read by intervals of 10 milliseconds. The programs breaks out of the while loop when the user presses the 'q' key
    if cv.waitKey(10) & 0xFF ==  ord('q'):
        break
    
# The following frees up resources and closes all windows
cap.release()

cv.destroyAllWindows()