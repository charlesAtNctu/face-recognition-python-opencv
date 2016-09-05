

import os.path, time
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

label2id = {}
id2label = {}

def get_images_and_labels(path):



    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    print image_paths;# user dir abs path here !!!
    print ""

    images = []
    labels = []

    label = 0;
    for image_path in image_paths:

        label2id[label] = image_path;
        id2label[image_path] = label;
        counter = 0;

        print image_path + " has label, " + str(label);
        # user_images = os.listdir(image_path)
        user_images = [os.path.join(image_path, f) for f in os.listdir(image_path) if not f.startswith('test_')]

        for user_image in user_images:
            #user_image_path = image_path + "/" + user_image;
            user_image_path = user_image;
            print "USER IMAGE PATH: " + user_image_path;
            user_image_pil = Image.open(user_image_path).convert('L') # Read the image and convert to grayscale
            user_image_np = np.array(user_image_pil, 'uint8') # Convert the image format into numpy array

            faces = faceCascade.detectMultiScale(user_image_np)
            for (x, y, w, h) in faces:
                images.append(user_image_np[y: y + h, x: x + w])
                labels.append(label)
                counter = counter + 1
                #cv2.imshow("Adding faces to traning set...", user_image_np[y: y + h, x: x + w])
                #cv2.waitKey(50)

        print "traing count: " + str(counter);
        print ""

        label = label + 1;

    return images, labels


def getMaxLastModified(path):

    maxLastModified = 0.0

    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    #print image_paths;
    #print ""

    for image_path in image_paths:
        #print image_path
        #print ""

        user_images = [os.path.join(image_path, f) for f in os.listdir(image_path) if not f.startswith('test_')]

        for user_image_file_path in user_images:
            #print user_image_file_path
            #print "1) last modified: %s" % time.ctime(os.path.getmtime(user_image_file_path))
            #print "2) last modified: %s" % os.path.getmtime(user_image_file_path)
            #print "3) last modified: %s" % round(os.stat(user_image_file_path).st_mtime)
            #print ""

            last_modified_time = os.path.getmtime(user_image_file_path)#round(os.stat(user_image_file_path).st_mtime)
            if last_modified_time > maxLastModified:
                maxLastModified = last_modified_time

    #print maxLastModified
    return maxLastModified



def main(argv):
    print cv2.__version__;

    face_dir_path = argv[1];
    test_image_dir_path = argv[2];
    dest_dir_path = argv[3];

    sofar_max_last_modified_time = 0
    while True:
        current_max_last_modified_time = getMaxLastModified(face_dir_path)
        if current_max_last_modified_time > sofar_max_last_modified_time:
            sofar_max_last_modified_time = current_max_last_modified_time
            images, labels = get_images_and_labels(face_dir_path)
            recognizer.train(images, np.array(labels))

        #image_path = "/var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/chuchi/face_cliu_20160901174419978.png"

        #print ""
        #print "given " + test_image_path;
        #print ""

        try:

            test_image_paths = [os.path.join(test_image_dir_path, f) for f in os.listdir(test_image_dir_path) if f.endswith('Recognize.png')]
            for test_image_path in test_image_paths:
                print "processing " + test_image_path;

                predict_image_pil = Image.open(test_image_path).convert('L')
                predict_image = np.array(predict_image_pil, 'uint8')
                faces = faceCascade.detectMultiScale(predict_image)

                print "# of faces: " + str(len(faces));
                print faces;

                for (x, y, w, h) in faces:
                    nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])

                    ## nbr_actual = id2label[test_image_path[0:test_image_path.rfind('/')]];#int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))

                    print "recognized as " + label2id[nbr_predicted][label2id[nbr_predicted].rfind('/')+1:] + ", " + str(conf)
                    print ""

                    ## if nbr_actual == nbr_predicted:
                    ##     print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
                    ## else:
                    ##     print "{} is Incorrect Recognized as {}".format(nbr_actual, nbr_predicted)

                print ""

                os.rename(test_image_path, dest_dir_path+test_image_path[test_image_path.rfind('/')+1:])


        except IOError, e:
            dummy = 0
            # print "might be caused by no such file exception ..." # continous print ... since commented it out ...

if __name__ == "__main__":
    main(sys.argv)

# python facerecognizer.py /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/

#                                                                       1                                   2                                                                                        3
# python facerecognizer2.py /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/ /var/nodes/easyrtc/node_modules/easyrtc/server_example/uploads/20160831174119477_localRecognize.png /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/
# add two table cell for log

#                                                                       1                                   2                                                                                        3
# python facerecognizer2.py /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/ /var/nodes/easyrtc/node_modules/easyrtc/server_example/uploads/ /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/
# add two table cell for log