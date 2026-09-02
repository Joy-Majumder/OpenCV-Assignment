from face_recognation import face_recognition
from track import face_tracking
from gender import age_gender
from obCount import object_counting
from ToolKit import image_processing

while True:
    print("1. Face Recognition")
    print("2. Multiple Face Tracking")
    print("3. Age/Gender Estimation")
    print("4. Object Counting")
    print("5. Image Processing")
    print("Q. Quit")
    choice = input("Choose: ")

    if choice == "1":
        face_recognition()
    elif choice == "2":
        face_tracking()
    elif choice == "3":
        age_gender()
    elif choice == "4":
        object_counting()
    elif choice == "5":
        image_processing()

    elif choice == "q":
        break