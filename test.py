"""
https://www.datacamp.com/tutorial/face-detection-python-opencv
"""

# Import OpenCV Package
import cv2

# Read  the images
imagePath = 'dad/IMG-20230105-WA0001.jpg'
img = cv2.imread(imagePath)

# Print dimensions of array
print(img.shape)

# Convert image to grayscale to improve comp eff
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)

# Load OpenCV's Haar Cascade classifier for frontal faces
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Detect faces on grayscale images using the classifier
face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

# Check if faces were detected
print("Faces found:", len(face))

# Draw a bounding box around the faces
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

# Display the image

# Convert image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plt.imshow(img_rgb)
plt.axis('off')
plt.show()