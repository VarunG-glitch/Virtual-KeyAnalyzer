from pynput.mouse import Listener
import os
import pyscreenshot

i = 0 # global variable to change the name of image as we click


def on_click(x, y, button, pressed):
    global i
    if pressed == True:
        img = pyscreenshot.grab(bbox=(x-17, y-17, x+20, y+20)) # This will grab the screenshot of a specified size bbox = (x1,y1,x2,y2)
        ans = os.getcwd() # This will be used to specify the location of the image
        ans = ans + '/' + str(i) + '.png' # manipulating this image to add the number along with image format
        img.save(ans)
        i += 1


def main():
    os.chdir(#include the path here) # This is used to add the picture to the specified directory
    with Listener(on_click=on_click) as listen: 
        listen.join()


if __name__ == "__main__":
    main()
