#!/usr/bin/python

import sys

def main(argv):

    #for x in argv:
    #    print x;

    src_dir = argv[0];
    prefix  = argv[1];
    dir_idx = argv[2];
    tgt_dir = argv[3];

    print 'source directory  : ', src_dir;
    print 'prefix to look for: ', prefix ;
    print 'directory index   : ', dir_idx;
    print 'target directory  : ', tgt_dir;


if __name__ == "__main__":
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    main(sys.argv)

#
# ubuntu@ip-172-31-46-108:~/GitHub/face-recognition-python-opencv$
# python moveFileByName.py /var/nodes/easyrtc/node_modules/easyrtc/server_example/uploads/ face_ 0 /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/
#
# arg1: /var/nodes/easyrtc/node_modules/easyrtc/server_example/uploads/
#
# arg2: face_, 0 (i.e., face)
#
# note: face_USERNAME_20160901110847330.png
#
# arg3: /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/
#
# note: create directory face and put it in this directory ...
#
########################################################################################################################
#
# ubuntu@ip-172-31-46-108:~/GitHub/face-recognition-python-opencv$
# python moveFileByName.py /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/ face_ 1 /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/
#
# arg1: /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/
#
# arg2: face_, 1 (i.e., username)
#
# note: face_USERNAME_20160901110847330.png
#
# arg3: /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face
#
# note: create directory USERNAME and put it in this directory ...
#