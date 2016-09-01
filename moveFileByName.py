#!/usr/bin/python

import sys

def main(argv):
    for x in argv:
        print x;

if __name__ == "__main__":
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    main(sys.argv)
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