import cv2

# video = cv2.VideoCapture(0)  # 0 - front camere
video = cv2.VideoCapture(1)  # 1 - rear camera

frames = 0
while True:
    frames += 1

    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capturing', gray)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(frames)

video.release()
cv2.destroyAllWindows()
