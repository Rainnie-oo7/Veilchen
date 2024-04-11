import cv2
import numpy as np

def detect_object(frame, object_keypoints, object_descriptors, orb):
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the keypoints and descriptors with ORB
    keypoints, descriptors = orb.detectAndCompute(gray_frame, None)

    # Create BFMatcher (Brute Force Matcher)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(object_descriptors, descriptors)

    # Sort them in ascending order of distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw matches on the frame
    img_matches = cv2.drawMatches(object_img, object_keypoints, frame, keypoints, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    return img_matches

# Capture video from camera
cap = cv2.VideoCapture(0)

# Load an object image for detection
object_img = cv2.imread('/home/boris/Pictures/Plek2.png', cv2.IMREAD_GRAYSCALE)

# Initiate ORB detector
orb = cv2.ORB_create()

# Find the keypoints and descriptors with ORB
object_keypoints, object_descriptors = orb.detectAndCompute(object_img, None)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Perform object detection
    result_frame = detect_object(frame, object_keypoints, object_descriptors, orb)

    # Display the resulting frame
    cv2.imshow('Object Detection with ORB', result_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
