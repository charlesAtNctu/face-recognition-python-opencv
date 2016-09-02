#!/usr/bin/python

import os, sys

#
# this link is important !!!
#
# http://docs.opencv.org/2.4/modules/contrib/doc/facerec/tutorial/facerec_video_recognition.html
#

def main(argv):

    print '***********************************************************************************************************';

    #for x in argv:
    #    print x;

    face_dir = argv[1];

    print 'face directory  : ', face_dir;

    users = os.listdir(face_dir)

    label = 0;

    for user_dir in users:
        print user_dir + " has label, " + str(label);
        images = os.listdir(face_dir+user_dir)
        for image in images:
            print face_dir + user_dir + "/" + image + ";" + str(label);
        label = label + 1;



    #    if file.startswith(prefix):
    #       # print file;
    #       segments = file.split('_');
    #       tgt_dir2 = tgt_dir + segments[int(dir_idx)] + "/"
    #
    #       # check if exists ...
    #       if not os.path.exists(tgt_dir2):
    #          print tgt_dir2 + " is being created !!!";
    #          os.makedirs(tgt_dir2);
    #
    #       os.rename(src_dir+file, tgt_dir2+file);


if __name__ == "__main__":
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    main(sys.argv)

# python createCSV.py /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/