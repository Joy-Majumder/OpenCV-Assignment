import cv2 as cv

def grayscale_image():
    path = "/Users/joy0x1/Downloads/UIU Mariner/Assignment/Ass2/ass/im1.jpeg"
    img = cv.imread(path)
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # this one gonna be used for gray color -,-
    # imgray = cv.cvtColor(img, cv.COLOR_BGR2RGB) # this one gonna be used for rbg color
    blur = cv.GaussianBlur(img, (7,7),0)
    resize = cv.resize(img, (500,500))
    rotate = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    cv.imshow("Original", img)
    cv.imshow("Grayscale", imgray)
    cv.imshow("Blur", blur)
    cv.imshow("Resize", resize)
    cv.imshow("Rotate", rotate)
    cv.waitKey(0)
    cv.destroyAllWindows()

grayscale_image()