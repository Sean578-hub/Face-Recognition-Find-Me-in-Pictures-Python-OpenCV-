# Face Recognition – Find Me in Pictures (Python + OpenCV)

## Project Description
This project uses face recognition to identify a specific person in a photo that contains multiple people.

The program loads a reference image of a person (Sean) and compares it with faces detected in another image. If the program finds a match, it highlights the face and labels it.

---

## Technologies
- Python
- OpenCV (cv2)
- face_recognition library

---

## How It Works
1. The program loads a reference image of Sean.
2. The face is converted into a numerical encoding.
3. A group image containing multiple people is loaded.
4. The program detects all faces in the group image.
5. Each detected face is compared with Sean's face encoding.
6. If a match is found, the face is labeled as "Sean".
7. The program draws rectangles and names around detected faces.

---

## How to Run

Install the required libraries:

pip install opencv-python  
pip install face_recognition  

Run the program:

python main.py

---

## Example Output
The program displays the image with rectangles drawn around detected faces.

- Sean's face is labeled **Sean** (green box)
- Other faces are labeled **Yan** (red box)

---

## Project Purpose
This project demonstrates how face recognition can be used to identify a specific person inside an image with multiple people.

It shows basic computer vision techniques using Python and OpenCV.

---

## Author
Sean Michaeli
