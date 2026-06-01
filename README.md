# Virtual-Mouse

An interesting project of making a virtual mouse using Python and its libraries.

## Features

- Recognize your hand
- Move the curson with just gestures
- Perform a click by finger gestures

## Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## How To Run

- Firstly import all the libraries mentioned abouve in a virtual environment in python file.
- Capture the video using OpenCV.
- Initialize the hand detection model and drawing utilities from MediaPipe to get hand and identify it.
- Use PyAutoGUI to move the mouse cursor to the position of the index finger tip and perform a click function.
