import cv2 as cv
import os
def grayscale_image():
    ok = os.getcwd()
    path = os.path.join(ok, '/Users/joy0x1/Downloads/UIU Mariner/Assignment/Ass2/ass/im1.jpeg')
    img = cv.imread(path)
    imgray = cv.cvtColor(img, cv.COLOR_BAYER_GR2BGRA)

    cv.imshow('image', imgray)
    cv.waitKey(0)

    print(img.shape)

if __name__ == '__main__':
    grayscale_image()