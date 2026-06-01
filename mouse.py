import cv2, mediapipe as mp, pyautogui

cap = cv2.VideoCapture(0)                               # Open the default camera
hand_detector = mp.solutions.hands.Hands()              # Initialize the hand detection model from MediaPipe
drawing_utils = mp.solutions.drawing_utils              # Initialize the drawing utilities from MediaPipe
screen_width, screen_height = pyautogui.size()          # Get the width and height of the screen
index_y = 0                                               # Initialize the y-coordinate of the index finger tip

while True:                                             # Continuously capture frames from the camera
    _, frame = cap.read()                               # Read a frame from the camera
    frame = cv2.flip(frame, 1)                          # Flip the frame horizontally for a mirror effect
    frame_height, frame_width, _ = frame.shape          # Get the height and width of the captured frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the captured frame from BGR to RGB color space
    output = hand_detector.process(rgb_frame)           # Process the RGB frame to detect hands
    hands = output.multi_hand_landmarks                 # Get the detected hand landmarks
    if hands:                                           # Print the detected hand landmarks to the console
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)   # Draw the detected hand landmarks on the original frame
            landmarks = hand.landmark                   # Get the landmarks of the detected hand
            for id, landmark in enumerate(landmarks):   # Print the ID and coordinates of each landmark
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                
                if id == 8:                             # If the landmark ID is 8 (tip of the index finger), draw a circle at that position
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))  # Draw a yellow circle at the position of the index finger tip
                    index_x = screen_width / frame_width * x     # Scale the x-coordinate of the index finger tip to the screen width
                    index_y = screen_height / frame_height * y   # Scale the y-coordinate of the
                    pyautogui.moveTo(index_x, index_y)           # Move the mouse cursor to the position of the index finger tip (scaled by a factor of 2)
                    
                if id == 4:                             # If the landmark ID is 4 (tip of the thumb), draw a circle at that position
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))  
                    thumb_x = screen_width / frame_width * x     
                    thumb_y = screen_height / frame_height * y   
                    if abs(index_y - thumb_y) < 20:     # If the distance between the index finger tip and thumb tip is less than 40 pixels, perform a mouse click
                        pyautogui.click()               # Perform a mouse click at the current cursor position
                        pyautogui.sleep(1)              # Sleep for 1 second to prevent multiple clicks from being registered
                
    cv2.imshow('Virtual Mouse', frame)                  # Display the captured frame in a window named 'Virtual Mouse'
    cv2.waitKey(1)                                      # Wait for 1 millisecond before capturing the next frame