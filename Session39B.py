import cv2, time
import numpy as np

video = cv2.VideoCapture(0)

frameCount = 0
while True:
    check, frame = video.read()
    frameCount += 1
    print(frame)
    cv2.imshow("MyVideo", frame)
    cv2.imshow("MyVideo", np.rot90(frame))

    key = cv2.waitKey(1) # 1 is 1 milisecond here

    if key == ord('q'):
        break

print(">> Total Frames Captured:", frameCount)
video.release()
cv2.destroyAllWindows()


# Assignment : Use OpenCV API and convert list of frames as video and save it:)
# explore opencv : https://docs.opencv.org/master/d9/df8/tutorial_root.html
