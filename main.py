import cv2
from PIL import ImageGrab

camera = cv2.VideoCapture(0)

i = 3

ds_factor = 0.5

while i > 0 :
    ret,frame = camera.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    img = cv2.flip(frame, 1)
    i = i - 1

cv2.imwrite('/users/hussainsalih/Desktop/fol/ud.png',img)

screen_img = ImageGrab.grab()

screen_img.save('/users/hussainsalih/Desktop/fol/comp.png','png')

camera.release()
cv2.destroyAllWindows()
