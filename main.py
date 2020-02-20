from PIL import ImageGrab

screen_img = ImageGrab.grab()

screen_img.save('screen.png','png')
