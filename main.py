from face_recognation import face_detect
from multiFace import multiple_face_tracking
from obCount import object_detect
from ToolKit import image_processing
from gender import gender
while True:

    print("1. Face Recognition")
    print("2. Multiple Face Tracking")
    print("3. Age/Gender Estimation")
    print("4. Object Counting")
    print("5. Image Processing : which is includes other things")
    print("Q. Quit")

    choice = input("Choose: ")

    if choice == "1":
        face_detect()
    elif choice == "2":
        multiple_face_tracking()
    elif choice == "3":
        gender()
    elif choice == "4":
        object_detect()
    elif choice == "5":
        image_processing()
    elif choice.lower() == "q":
        break