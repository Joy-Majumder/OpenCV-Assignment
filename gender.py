import cv2 as cv

def gender():
    camera = cv.VideoCapture(0)
    face_capture = cv.CascadeClassifier(
        "/Users/joy0x1/Downloads/UIU Mariner/Assignment/Ass2/cascadeFile/haarcascade_frontalface_default.xml"
    )
    gModel = cv.dnn.readNetFromONNX("/Users/joy0x1/Downloads/UIU Mariner/Assignment/Ass2/models/gender_googlenet.onnx")
    genderList = ['Male', 'Female']
    while True:
        read, vdo = camera.read()
        vdo = cv.flip(vdo, 1)
        gray = cv.cvtColor(vdo, cv.COLOR_BGR2GRAY)
        face = face_capture.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(40, 40),flags=cv.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in face:
            face_img = vdo[y:y+h, x:x+w]
            bloo = cv.dnn.blobFromImage(face_img,1,(227, 227),(78.4263377603, 87.7689143744, 114.895847746),swapRB=False
            )
            gModel.setInput(bloo)
            pred = gModel.forward()
            gender = genderList[pred[0].argmax()]
            cv.rectangle(vdo,(x, y),(x+w, y+h),(0, 0, 0),2
            )
            cv.putText(vdo,gender,(x, y - 10),cv.FONT_HERSHEY_SIMPLEX,0.7,(0, 0, 0),2
            )
        cv.imshow("Gender Estimation", vdo)
        if cv.waitKey(10) == ord("a"):
            break
    camera.release()
    cv.destroyAllWindows()