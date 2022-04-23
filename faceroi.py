import cv2


def record_face_detection(path, in_file, out_file):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap_rec = cv2.VideoCapture(path+in_file)
    cap_rec.set(3,640)
    cap_rec.set(4,480)

    frame_count_rec = cap_rec.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Frame out :recorded : ", frame_count_rec)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path+out_file, fourcc, 20.0, (640,480))


    frame_count_read = 0
    while True :
        ret2, frame_rec = cap_rec.read()
        if ret2:

            gray = cv2.cvtColor(frame_rec, cv2.COLOR_BGR2GRAY)
            # Detect the faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame_rec, (x, y), (x + w, y + h), (255, 0, 0), 2)
                out.write(frame_rec)


            #cv2.imshow('Faces ', frame_rec)

            frame_count_read += 1
            # Press Q on keyboard to  exit
            #if cv2.waitKey(25) & 0xFF == ord('q'):
            #    print("q pressed")
            #    break
        else:
            print("Recorded frame empty")
            break

    cap_rec.release()
    out.release()
    cv2.destroyAllWindows()

    print( "Frame Count read: ", frame_count_read)