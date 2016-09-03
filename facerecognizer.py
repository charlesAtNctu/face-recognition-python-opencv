


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



    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    print image_paths;# user dir abs path here !!!

    images = []
    labels = []

    label = 0;
    for image_path in image_paths:

        print image_path + " has label, " + str(label);
        user_images = os.listdir(image_path)
        for user_image_path in user_images:
            print user_image_path;
            user_image_pil = Image.open(user_image_path).convert('L')# Read the image and convert to grayscale
        label = label + 1;



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

# python facerecognizer.py /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/



