import cv2
import numpy as np
import pygame

# Initialize Pygame
pygame.mixer.init()
sound = pygame.mixer.Sound('smash.wav')  

# Initialize camera
cap = cv2.VideoCapture(0)  # Use 0 for default camera

# Define theex region where you want to trigger the sound
region_x, region_y, region_width, region_height = 100, 100, 200, 200

while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define a range of skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Threshold the HSV image to get only skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # If the area is greater than a threshold, consider it as a hand
        if area > 1000:
            # Find the centroid of the hand
            M = cv2.moments(contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            # Draw a circle at the centroid
            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

            # Check if the centroid is within the predefined region
            if region_x < cx < region_x + region_width and region_y < cy < region_y + region_height:
                # Play the sound
                sound.play()

    # Draw the predefined region
    cv2.rectangle(frame, (region_x, region_y), (region_x + region_width, region_y + region_height), (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Hand Tracking', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
