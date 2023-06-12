import cv2
pic = cv2.imread('image2.jpg')
window_name = 'Image processing'
grey = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey, invertedblur, scale=256.0)
# cv2.imshow(window_name, sketch)
cv2.imwrite('output_image.jpg', sketch)

