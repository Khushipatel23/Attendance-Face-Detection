import cv2
import webbrowser


def openExcel():
    webbrowser.open("C:/Users/shaha/Documents/Projects/Face Detection/Attendance.csv")


def captureImage(name):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow('Webcam',frame)
    cv2.waitKey(500)
    cv2.imwrite(f'database/{name}.jpg', frame)



