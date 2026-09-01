import cv2 as cv
import os
def grayscale_image():
    ok = os.getcwd()
    path = os.path.join(ok, '/Users/joy0x1/Downloads/UIU Mariner/Assignment/Ass2/ass/im1.jpeg')
    img = cv.imread(path)
    # imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # this one gonna be used for gray color -,-
    # imgray = cv.cvtColor(img, cv.COLOR_BGR2RGB) # this one gonna be used for rbg color
    imgray = cv.cvtColor(img, cv.COLOR_BGR2LAB) # this one gonna be used for rbg color

    cv.imshow('image', imgray)
    cv.waitKey(0)

    print(img.shape)


grayscale_image()