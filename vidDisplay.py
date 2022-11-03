import cv2

img = cv2.imread("galaxy.jpg", 0)

#Basic checks
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img,(1000, 500))
cv2.imshow("Galaxy", img)
cv2.waitKey(2000)
cv2.destroyAllWindows()