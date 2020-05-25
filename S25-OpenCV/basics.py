import cv2

img = cv2.imread('galaxy.jpg', 0)  # 0 - grayscale

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow('Galaxy', resized_img)
# cv2.waitKey(2000) # 2 sec
cv2.waitKey(0)  # until any key is pressed
cv2.destroyAllWindows()

cv2.imwrite('resized_Galaxy.jpg', resized_img)
