import cv2
import face_recognition

Sean = face_recognition.load_image_file("Sean.jpg")
sean_encoding = face_recognition.face_encodings(Sean)[0]

Sean_Yan = face_recognition.load_image_file("Sean And Yan.jpg")
Sean_Yan_encoding = face_recognition.face_encodings(Sean_Yan)
Sean_Yan_loc = face_recognition.face_locations(Sean_Yan)
sean_yan_bgr = cv2.cvtColor(Sean_Yan, cv2.COLOR_RGB2BGR)



for (face_encoding, (top, right, bottom, left)) in zip(Sean_Yan_encoding, Sean_Yan_loc):
    match = face_recognition.compare_faces([sean_encoding], face_encoding)[0]
    if match:
        name = "Sean"
        color = (0, 255, 0)
    else:
        name = "Yan"
        color = (0, 0, 255)

    cv2.rectangle(sean_yan_bgr, (left, top), (right, bottom), color, 2)
    cv2.putText(sean_yan_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

cv2.imwrite("Sean And yan finder.jpg", sean_yan_bgr)
cv2.imshow("Sean And Yan.jpg", sean_yan_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()


