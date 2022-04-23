import cv2


def display_video(path, file):

    cap_rec = cv2.VideoCapture(path+file)
    cap_rec.set(3,640)
    cap_rec.set(4,480)

    frame_count_rec = cap_rec.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Frame out :recorded : ", frame_count_rec)

    frame_count_read = 0
    while True :
        ret2, frame_rec = cap_rec.read()
        if ret2:
            cv2.imshow('Recorded ', frame_rec)
            frame_count_read += 1
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            print("Recorded frame empty")
            break

    cap_rec.release()
    cv2.destroyAllWindows()

    print( "Frame Count read: ", frame_count_read)