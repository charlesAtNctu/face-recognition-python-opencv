


import cv2, os, sys
import numpy as np
from PIL import Image

# For face detection we will use the Haar Cascade provided by OpenCV.
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# recognizer = cv2.face.createEigenFaceRecognizer();
# recognizer = cv2.face.createFisherFaceRecognizer();
# For face recognition we will the the LBPH Face Recognizer
recognizer = cv2.face.createLBPHFaceRecognizer();
def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]

    print image_paths;

    # # images will contains face images
    # images = []
    # # labels will contains the label that is assigned to the image
    # labels = []
    # for image_path in image_paths:
    #     # Read the image and convert to grayscale
    #     image_pil = Image.open(image_path).convert('L')
    #     # Convert the image format into numpy array
    #     image = np.array(image_pil, 'uint8')
    #     # Get the label of the image
    #     nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
    #     # Detect the face in the image
    #     faces = faceCascade.detectMultiScale(image)
    #     # If face is detected, append the face to images and the label to labels
    #     for (x, y, w, h) in faces:
    #         images.append(image[y: y + h, x: x + w])
    #         labels.append(nbr)
    #         cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
    #         cv2.waitKey(50)
    # # return the images list and labels list
    # return images, labels


def main(argv):
    print cv2.__version__;
    face_dir_path = argv[1];
    get_images_and_labels(face_dir_path)

if __name__ == "__main__":
    main(sys.argv)






