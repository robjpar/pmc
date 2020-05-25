import cv2
import glob

images = glob.glob('*.jpg')
print(images)

for image in images:
    if image[:8] == 'resized_':
        continue

    img = cv2.imread(image, 1)  # 1 - color
    cv2.imshow('Original', img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    re = cv2.resize(img, (int(img.shape[1]/4), int(img.shape[0]/4)))
    cv2.imshow('Resized', re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    cv2.imwrite('resized_'+image, re)
