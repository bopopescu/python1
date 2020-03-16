import cv2
import numpy as np
image = cv2.imread("nature.jpg", 1)   # 0 Black and White

print("+++Original Image+++")
print(image)

print("+++Original Image+++")
shape = image.shape
print(shape)

resizedImage = cv2.resize(image, (shape[1]//2, shape[0]//2))
print("+++Resized Image+++")
print(resizedImage)

print("+++Resized Image+++")
resizedShape = resizedImage.shape
print(resizedShape)
np.rot90(resizedImage)

cv2.imshow("Resized nature", resizedImage)

cv2.imwrite("Mynature.jpg", resizedImage)
cv2.imwrite("Mynature90.jpg", resizedImage)
print("Mynature saved")

cv2.waitKey(0)

cv2.destroyAllWindows()