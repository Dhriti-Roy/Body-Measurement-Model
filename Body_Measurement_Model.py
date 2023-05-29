# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.WARNING)

"""

@author: Dhriti

"""
import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector
import time

# Define constants for body measurement
BODY_PARTS = {"right_shoulder": 2, "left_shoulder": 5, "right_hip": 8, "left_hip": 11, "neck": 1, "right_forearm": 4, "left_forearm": 7, "right_upperarm": 3, "left_upperarm": 6, "right_wrist": 4, "left_wrist": 7, "chest": 28,  "right_elbow": 3, "left_elbow": 6,"neck": 1,"nose": 0}


# Take input for rectangle size
rect_size = 1

# Instantiate the PoseDetector class
detector = PoseDetector()

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Set the frame size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

# Start the timer
start_time = time.time()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Find the pose points and draw them on the image
    img = detector.findPose(frame)
    
    # Get the pose points coordinates and bounding box information
    lmlist, bboxInfo = detector.findPosition(img)

    if lmlist:
        # Draw rectangles around detected body parts
        for part, index in BODY_PARTS.items():
            x, y = lmlist[index][1], lmlist[index][2]
            cv2.rectangle(frame, (x - rect_size, y - rect_size), (x + rect_size, y + rect_size), (0, 255, 0), 2)

        # Measure length
        right_shoulder = np.array([lmlist[BODY_PARTS["right_shoulder"]][1], lmlist[BODY_PARTS["right_shoulder"]][2]])
        left_shoulder = np.array([lmlist[BODY_PARTS["left_shoulder"]][1], lmlist[BODY_PARTS["left_shoulder"]][2]])
        right_hip = np.array([lmlist[BODY_PARTS["right_hip"]][1], lmlist[BODY_PARTS["right_hip"]][2]])
        left_hip = np.array([lmlist[BODY_PARTS["left_hip"]][1], lmlist[BODY_PARTS["left_hip"]][2]])
        
        #Measure shoulder-to-hip and right-to-left-shoulder
        shoulder_to_hip = np.linalg.norm(right_shoulder - right_hip)
        shoulder_to_shoulder = np.linalg.norm(right_shoulder - left_shoulder)
        #waist measurement
        waist = np.linalg.norm(right_hip - left_hip)/3
        
        if lmlist:
            # Calculate body measurements
            neck_girth = np.linalg.norm(np.array([lmlist[BODY_PARTS["right_shoulder"]][1], lmlist[BODY_PARTS["right_shoulder"]][2]]) - np.array([lmlist[BODY_PARTS["neck"]][1], lmlist[BODY_PARTS["neck"]][2]]))
            right_forearm_length = np.linalg.norm(np.array([lmlist[BODY_PARTS["right_elbow"]][1], lmlist[BODY_PARTS["right_elbow"]][2]]) - np.array([lmlist[BODY_PARTS["right_wrist"]][1], lmlist[BODY_PARTS["right_wrist"]][2]]))
            left_forearm_length = np.linalg.norm(np.array([lmlist[BODY_PARTS["left_elbow"]][1], lmlist[BODY_PARTS["left_elbow"]][2]]) - np.array([lmlist[BODY_PARTS["left_wrist"]][1], lmlist[BODY_PARTS["left_wrist"]][2]]))
            right_upperarm_length = np.linalg.norm(np.array([lmlist[BODY_PARTS["right_shoulder"]][1], lmlist[BODY_PARTS["right_shoulder"]][2]]) - np.array([lmlist[BODY_PARTS["right_elbow"]][1], lmlist[BODY_PARTS["right_elbow"]][2]]))
            left_upperarm_length = np.linalg.norm(np.array([lmlist[BODY_PARTS["left_shoulder"]][1], lmlist[BODY_PARTS["left_shoulder"]][2]]) - np.array([lmlist[BODY_PARTS["left_elbow"]][1], lmlist[BODY_PARTS["left_elbow"]][2]]))
            arm_length = right_upperarm_length + right_forearm_length
            sleeve_length = arm_length - np.linalg.norm(np.array([lmlist[BODY_PARTS["right_elbow"]][1], lmlist[BODY_PARTS["right_elbow"]][2]]) - np.array([lmlist[BODY_PARTS["right_wrist"]][1], lmlist[BODY_PARTS["right_wrist"]][2]]))
           
        
        # Measure waist size
        #ribcage = np.array([lmlist[28][1], lmlist[28][2]]) # bottom of the ribcage
        #hip_midpoint = (right_hip + left_hip) // 2 # midpoint between left and right hip
        #waist = np.linalg.norm(ribcage - hip_midpoint)
        
        # Measure waist size
        #pubic_bone = np.array([lmlist[BODY_PARTS["pubic_bone"]][1], lmlist[BODY_PARTS["pubic_bone"]][2]])
        #hip_midpoint = (right_hip + left_hip) // 2 - np.array([0, pubic_bone_offset])
        #ribcage = np.array([lmlist[28][1], lmlist[28][2]])
        #waist = np.linalg.norm(ribcage - hip_midpoint)

        # Check if one minute has passed
        if time.time() - start_time >= 10:
            # Print body measurements
            print("Shoulder to Hip Length: ", shoulder_to_hip)
            print()
            print("Shoulder to Shoulder Length: ", shoulder_to_shoulder)
            print()
            print("Waist Measurement: ", waist)
            print()
            print("Neck Girth: ", neck_girth)
            print()
            print("Right Forearm Length: ", right_forearm_length)
            print()
            print("Left Forearm Length: ", left_forearm_length)
            print()
            print("Right Upperarm Length: ", right_upperarm_length)
            print()
            print("Left Upperarm Length: ", left_upperarm_length)
            print()
            print("Arm Length: ",  arm_length)
            print()
            print("Sleeve Length: ", sleeve_length)
         
            break

    else:
        print("No body parts detected.")

    # Display the resulting image
    cv2.imshow('frame', frame)

    # Check if the user has closed the window or pressed the 'q' key
    key = cv2.waitKey(1)
    if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1 or key == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
