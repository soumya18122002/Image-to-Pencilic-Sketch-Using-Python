import cv2
from PIL import Image
image = cv2.imread("anime.jpg")
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert,(21,21),10)
invertblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img,invertblur,scale=256.0)
cv2.imwrite("sketch.png",sketch)

img_file = "sketch.png"
img = Image.open(img_file)
img.show(img)