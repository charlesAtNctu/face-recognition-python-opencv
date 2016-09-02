import cv2, os
import numpy as np
#from PIL 
import Image

print cv2.__version__;

recognizer = cv2.face.createLBPHFaceRecognizer();
recognizer = cv2.face.createLBPHFaceRecognizer();
recognizer = cv2.face.createEigenFaceRecognizer();
recognizer = cv2.face.createFisherFaceRecognizer();

