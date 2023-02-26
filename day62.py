# import cv2
#
# vid = cv2.VideoCapture(0)
# # print(type(vid))
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = vid.read()
#     # Display the resulting frame
#     cv2.imshow('preview',frame)
#     # Waits for a user input to quit the application
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# vid.release()
# cv2.destroyAllWindows()
import cv2
import sys

# faceCascade = cv2.CascadeClassifier(1)
#
# video_capture = cv2.VideoCapture(0)
#
# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.cv.CV_HAAR_SCALE_IMAGE
#     )
#
#     # Draw a rectangle around the faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#     # Display the resulting frame
#     cv2.imshow('Video', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows()

# class Employee:
#     def __init__(self):
#         self.__name = "Nur Nahian"
#
#
# a = Employee()
#
#
# print(a._Employee__name)

import random


def check( comp, user):
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1
    return 1


comp = random.randint(0, 2)

user = int(input("0 for Snake, 1 for Water and 2 for Gun\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if score == 0:
    print("It a draw")
elif score == -1:
    print("You lose")
else:
    print("You Win")
