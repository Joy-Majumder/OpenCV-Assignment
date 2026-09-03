import cv2 as cv
from ultralytics import YOLO as yo

def object_detect():
    camera = cv.VideoCapture(0) # camera on with this
    model = yo("/Users/joy0x1/Downloads/UIU Mariner/Assignment/Ass2/models/yolo11n.pt")
    while True:
        read, vdo = camera.read()
        vdo = cv.flip(vdo, 1)
        results = model(vdo)
        # color = cv.cvtColor(vdo,cv.COLOR_BGR2GRAY)
        # face = face_capture.detectMultiScale(
        for result in results:
            for box in result.boxes:
                x1,y1,x2,y2 = map(int, box.xyxy[0]) 
                class_id = int(box.cls[0])
                name = model.names[class_id]
                cv.rectangle(vdo, (x1,y1), (x2,y2),(0,255,0),2)
                cv.putText(vdo,name,(x1,y1 - 10),
                           cv.FONT_HERSHEY_SIMPLEX,0.7,(0, 0, 0),2)
        cv.imshow("Object Detect:", vdo)
        if cv.waitKey(10) == ord("a"):
            break

    camera.release()
    cv.destroyAllWindows()
