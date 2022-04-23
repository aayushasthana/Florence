import cv2


def capture_live(path, filename):

    cap_live = cv2.VideoCapture(0)
    cap_live.set(3,640)
    cap_live.set(4,480)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path+filename, fourcc, 20.0, (640,480))

    frame_count_live = 0
    while True:
        ret, frame_live = cap_live.read()
        out.write(frame_live)
        cv2.imshow('Live', frame_live)
        frame_count_live += 1
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            print("Frame out :Live : ", frame_count_live)
            break

    cap_live.release()
    out.release()
    cv2.destroyAllWindows()
