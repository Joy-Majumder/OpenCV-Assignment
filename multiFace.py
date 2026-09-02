import cv2 as cv


def multiple_face_tracking():

    camera = cv.VideoCapture(0)

    face_capture = cv.CascadeClassifier(
        "/Users/joy0x1/Downloads/UIU Mariner/Assignment/Ass2/cascadeFile/haarcascade_frontalface_default.xml"
    )
    while True:
        read, vdo = camera.read()
        vdo = cv.flip(vdo, 1)
        gray = cv.cvtColor(vdo, cv.COLOR_BGR2GRAY)
        face = face_capture.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40),
                flags = cv.CASCADE_SCALE_IMAGE
                )

        for(x,y,w,h) in face:
            cv.rectangle(vdo, (x,y), (x+w, y+h),(0,255,0),2)

            cv.putText(
                vdo,f"Face {i + 1}",(x, y - 10),cv.FONT_HERSHEY_SIMPLEX,0.7,(0, 255, 0),2)
        cv.putText(vdo,f"Faces: {len(face)}",(20, 40),
            cv.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0),2)
        cv.imshow("Multiple Face Tracking", vdo)

        if cv.waitKey(10) == ord("a"):
            break

    camera.release()
    cv.destroyAllWindows()

multiple_face_tracking()