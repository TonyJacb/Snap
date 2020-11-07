## What is Snap?

Snap is a simple attempt to make a Google Lens clone ie a point and shoot object detector that also brings up relevant results based on the object. For now only features such as Object class and color of the object has been implemented.

## Setup

Follow [this](https://www.youtube.com/watch?v=aimSGOAUI8Y) till after the execution of `get_pi_requirements.sh` to get started with your Python environment.
To make this program mobile, I downloaded IPWebcam for my Android phone and fed the camera input to the TFlite model. The main script is a modification of the `TFlite_detection_video.py` script from [Edje Electronics](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi)

## Block Diagram
![Block Diagram](https://github.com/TonyJac/Snap/blob/master/Group_5.png)
