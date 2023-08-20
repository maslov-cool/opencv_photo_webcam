import cv2

video = cv2.VideoCapture(0)
video.set(3, 800)
video.set(4, 600)

while True:
    success, img = video.read()
    cv2.imshow('Water', img)

    key = cv2.waitKey(1)

    if key == ord('c'):
        break
