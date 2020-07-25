import cv2
import numpy as np
import face_recognition

imgSsr = face_recognition.load_image_file('images/Sushant Singh.jpg')
imgSsr = cv2.cvtColor(imgSsr, cv2.COLOR_BGR2RGB)
encodeSsr = face_recognition.face_encodings(imgSsr)[0]
faceDetectSsr = face_recognition.face_locations(imgSsr)[0]

imgSsrTest = face_recognition.load_image_file('testImages/Sushant Singh.jpg')
imgSsrTest = cv2.cvtColor(imgSsrTest, cv2.COLOR_BGR2RGB)
encodeSsrTest = face_recognition.face_encodings(imgSsrTest)[0]
faceDetectSsrTest = face_recognition.face_locations(imgSsrTest)[0]


cv2.rectangle(imgSsr, (faceDetectSsr[3], faceDetectSsr[0]), (faceDetectSsr[1], faceDetectSsr[2]), (80, 127, 255), 1)
cv2.rectangle(imgSsrTest, (faceDetectSsrTest[3], faceDetectSsrTest[0]), (faceDetectSsrTest[1], faceDetectSsrTest[2]), (80, 127, 255), 1)

result = face_recognition.compare_faces([encodeSsr], encodeSsrTest)
faceDistance = face_recognition.face_distance([encodeSsr],encodeSsrTest)

cv2.putText(imgSsrTest, f'{result} {faceDistance}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (80, 127, 255))
cv2.imshow('Training', imgSsr)
cv2.imshow('Test', imgSsrTest)
print(result, faceDistance)

cv2.waitKey(0)