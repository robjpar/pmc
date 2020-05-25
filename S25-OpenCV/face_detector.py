import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('photo.jpg')
img = cv2.imread('news.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Grayscale', grayscale_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

faces = face_cascade.detectMultiScale(
    grayscale_img,
    # scaleFactor=1.05,
    scaleFactor=1.1,
    minNeighbors=5
)

print(type(faces))
print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow('Color', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
