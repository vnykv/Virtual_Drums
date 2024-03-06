import cv2
import numpy as np
import imutils
import pygame  # Import pygame for sound playback

# Initialize Pygame mixer
pygame.mixer.init()

# Load your drum sounds
sound_ride = pygame.mixer.Sound('ride.wav')
sound_ride_bell = pygame.mixer.Sound('ride_bell.wav')
sound_hi_hat_close = pygame.mixer.Sound('hi_hat_close.wav')
sound_crash = pygame.mixer.Sound('crash.wav')
sound_snare = pygame.mixer.Sound('snare.wav')
sound_snare_rim = pygame.mixer.Sound('snare_rim.wav')
sound_hi_hat = pygame.mixer.Sound('hi_hat.wav')
sound_hi_hat_open = pygame.mixer.Sound('hi_hat_open.wav')
sound_tom_hi = pygame.mixer.Sound('tom_hi.wav')
sound_tom_mid = pygame.mixer.Sound('tom_mid.wav')
sound_tom_low = pygame.mixer.Sound('tom_low.wav')
sound_kick = pygame.mixer.Sound('kick.wav')


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, height=700, width=900)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define your color ranges for detection
    low_red = np.array([131, 90, 106])
    high_red = np.array([255, 255, 255])

    low_blue = np.array([40, 150, 116])
    high_blue = np.array([255, 255, 255])

    # Create masks for color detection
    red_mask = cv2.inRange(hsv, low_red, high_red)
    blue_mask = cv2.inRange(hsv, low_blue, high_blue)

     # image/frame, start_point, end_point, color, thickness
    cv2.rectangle(frame, (0,0), (200,150), (255,0,0),1)
    cv2.putText(frame,'RIDE',(70,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (210,0), (430,150), (0,0,255),1)
    cv2.putText(frame,'RIDE BELL',(245,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    cv2.rectangle(frame, (440,0), (650,150), (255,0,0),1)
    cv2.putText(frame,'HITHAT close',(445,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (660,0), (900,150), (0,0,255),1)
    cv2.putText(frame,'CRASH',(730,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)


    cv2.rectangle(frame, (0,160), (50,370), (255,0,0),1)
    cv2.putText(frame,'SNARE',(10,290),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (0,380), (50,570), (0,0,255),1)
    cv2.putText(frame,'SNARE RIM',(10,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    
    cv2.rectangle(frame, (850,160), (900,370), (255,0,0),1)
    cv2.putText(frame,'HIT HAT',(770,290),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (850,380), (900,570), (0,0,255),1)
    cv2.putText(frame,'HIT HAT OPEN',(670,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)


    cv2.rectangle(frame, (0,580), (200,700), (255,0,0),1)
    cv2.putText(frame,'TOM HI',(50,640),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (210,580), (430,700), (0,0,255),1)
    cv2.putText(frame,'TOM MID',(250,640),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    cv2.rectangle(frame, (440,580), (650,700), (255,0,0),1)
    cv2.putText(frame,'TOM LOW',(480,640),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (660,580), (900,700), (0,0,255),1)
    cv2.putText(frame,'KICK',(740,640),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    # Detect and handle red object
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        print((x,y))  
        
        if x > 0 and y > 0 and x < 100 and y < 100:
            sound_ride.play()
            break      
        elif x > 100 and y > 0  and x < 200 and y < 100:
            sound_ride_bell.play()
            break      
        elif x > 200 and y > 0  and x < 300 and y < 100:
            sound_hi_hat_close.play()
            break      
        elif x > 300 and y > 0 and x < 400 and y < 100:
            sound_crash.play()
            break
        elif x > 400 and y > 0 and x < 500 and y < 100:
            sound_snare.play()
            break
        elif x > 500 and y > 0 and x < 600 and y < 100:
            sound_snare_rim.play()
            break
        elif x > 600 and y > 0 and x < 700 and y < 100:
            sound_hi_hat.play()
            break
        elif x > 700 and y > 0 and x < 800 and y < 100:
            sound_hi_hat_open.play()
            break
        elif x > 800 and y > 0 and x < 900 and y < 100:
            sound_tom_hi.play()
            break
        elif x > 0 and y > 100 and x < 100 and y < 200:
            sound_tom_mid.play()
            break
        elif x > 100 and y > 100 and x < 200 and y < 200:
            sound_tom_low.play()
            break
        elif x > 200 and y > 100 and x < 300 and y < 200:
            sound_kick.play()
            break

    # Detect and handle blue object
    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        print((x,y))
        
        if x > 0 and y > 0 and x < 100 and y < 100:
            sound_ride.play()
            break      
        elif x > 100 and y > 0  and x < 200 and y < 100:
            sound_ride_bell.play()
            break      
        elif x > 200 and y > 0  and x < 300 and y < 100:
            sound_hi_hat_close.play()
            break      
        elif x > 300 and y > 0 and x < 400 and y < 100:
            sound_crash.play()
            break
        elif x > 400 and y > 0 and x < 500 and y < 100:
            sound_snare.play()
            break
        elif x > 500 and y > 0 and x < 600 and y < 100:
            sound_snare_rim.play()
            break
        elif x > 600 and y > 0 and x < 700 and y < 100:
            sound_hi_hat.play()
            break
        elif x > 700 and y > 0 and x < 800 and y < 100:
            sound_hi_hat_open.play()
            break
        elif x > 800 and y > 0 and x < 900 and y < 100:
            sound_tom_hi.play()
            break
        elif x > 0 and y > 100 and x < 100 and y < 200:
            sound_tom_mid.play()
            break
        elif x > 100 and y > 100 and x < 200 and y < 200:
            sound_tom_low.play()
            break
        elif x > 200 and y > 100 and x < 300 and y < 200:
            sound_kick.play()
            break

    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:  # ESC key to break
        break

cap.release()
cv2.destroyAllWindows()
