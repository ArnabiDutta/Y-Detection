# Y-Detect: Letter Y Pose Estimation with OpenCV

## Overview
Y-Detect is an OpenCV-based computer vision project designed to detect the letter 'Y' from an image or a live video feed. It calculates the orientation angle of the detected shape and marks its centroid, providing insights into object positioning and recognition.

## Features
- **Letter 'Y' detection** from an input image.
- **Contour analysis** using OpenCV to extract shape features.
- **Shape matching** to recognize 'Y' in real-time.
- **Angle estimation** to determine the orientation of the detected letter.
- **Live camera feed support** for real-time detection and analysis.

## Technologies Used
- **OpenCV**: Image processing and computer vision.
- **NumPy**: Array operations and mathematical functions.
- **Python**: Programming language for implementation.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ArnabiDutta/Y-Detect.git
   cd Y-Detect
   ```
2. Install required dependencies:
   ```bash
   pip install opencv-python numpy
   ```
3. Run the detection script:
   ```bash
   python detect_Y.py
   ```

## How It Works
1. **Image Processing:**
   - Converts the image to grayscale.
   - Applies Canny edge detection.
   - Extracts contours and matches them to a predefined reference shape ('Y').
2. **Real-Time Detection:**
   - Captures live feed from the webcam.
   - Detects and highlights the letter 'Y' in real time.
   - Computes the angle of the detected letter.
   - Displays the detection result with annotations.

## Usage
- Press 'q' to exit the live detection window.
- Modify the input image path in the script to test with different images.

## Example Output
- **Detected Letter 'Y' Contours:** Green outline.
- **Bounding Box:** Red rectangle around detected shape.
- **Center Point:** Black dot marking the centroid.
- **Angle Display:** Text annotation showing the computed orientation angle.

## Future Improvements
- Improve accuracy for different fonts and handwritten letters.
- Implement a machine learning model for more robust recognition.
- Extend to detect multiple letters or shapes in an image.

## Author
Developed by **Arnabi Dutta**. This is just an introductory project to learn OpenCv. Contributions and improvements are welcome!

