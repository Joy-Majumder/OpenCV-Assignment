from face_recognation import face_detect
from multiFace import multiple_face_tracking
from ToolKit import image_processing

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
        print("Age/Gender coming soon")
    elif choice == "4":
        print("Object counting coming soon")
    elif choice == "5":
        image_processing()
    elif choice.lower() == "q":
        break