import cv2
from capture import capture_live
from display import display_video
from faceroi import record_face_detection


print("Start ...")

print("Capture ..start")
capture_live("",'face.mp4')
print("Capture ..done")


print("Display ..start")
display_video("",'face.mp4')
print("Display ..done")


print("Face detection..start")
record_face_detection("",'face.mp4', 'facedetect.mp4')
print("Face detection..done")


print("Display ..start")
display_video("",'facedetect.mp4')
print("Display ..done")







