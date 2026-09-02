import cv2 as cv

def face_detect():
    camera = cv.VideoCapture(0) # camera on with this
    face_capture = cv.CascadeClassifier('/Users/joy0x1/Downloads/UIU Mariner/Assignment/Ass2/cascadeFile/haarcascade_frontalface_default.xml')

    while True:
        read, vdo = camera.read()
        vdo = cv.flip(vdo, 1)
        color = cv.cvtColor(vdo,cv.COLOR_BGR2GRAY)
        face = face_capture.detectMultiScale(
        color, scaleFactor=1.1, minNeighbors=5, minSize=(40,40),
        flags = cv.CASCADE_SCALE_IMAGE
        )
        for(x,y,w,h) in face:
            cv.rectangle(vdo, (x,y), (x+w, y+h),(0,255,0),2)

        cv.imshow("Face Recog.", vdo)
        if cv.waitKey(10) == ord("a"):
            break

    camera.release()
    cv.destroyAllWindows()
