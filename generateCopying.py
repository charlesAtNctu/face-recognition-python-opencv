#!/usr/bin/python

import os, sys
import time
from shutil import copyfile

def main(argv):

    copying_dir = argv[1];
    src_file = argv[2];
    tgt_file = argv[3];

    count = 0
    while (count < 30):
        count = count + 1
        print "" + str(count) + "\t: copying " + copying_dir+src_file + " " + copying_dir+tgt_file
        copyfile(copying_dir+src_file, copying_dir+tgt_file)
        time.sleep(1)

if __name__ == "__main__":
    main(sys.argv)