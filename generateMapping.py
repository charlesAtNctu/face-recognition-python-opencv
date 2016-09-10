#!/usr/bin/python

import os, sys

def main(argv):

    mapping_dir = argv[1];

    print 'mapping directory  : ', mapping_dir;

    c2e_mappings = os.listdir(mapping_dir)# todo: create c2e and e2c ...
    for c2e_mapping in c2e_mappings:
       if c2e_mapping.startswith("c2e_") and c2e_mapping.endswith(".mapping"):

          first_underscore_idx= c2e_mapping.find("_");
          second_underscore_idx = c2e_mapping.rfind("_");
          dot_idx = c2e_mapping.rfind(".");

          cookieid = c2e_mapping[first_underscore_idx+1:second_underscore_idx];
          easyrtcid = c2e_mapping[second_underscore_idx+1:dot_idx]

          e2e_mappings = os.listdir(mapping_dir)
          for e2e_mapping in e2e_mappings:
             if e2e_mapping.startswith("e2e_") and e2e_mapping.endswith(".mapping"):

                 first_underscore_idx2 = e2e_mapping.find("_");
                 second_underscore_idx2 = e2e_mapping.rfind("_");
                 dot_idx2 = e2e_mapping.rfind(".");

                 src_easyrtcid = e2e_mapping[first_underscore_idx2+1:second_underscore_idx2];
                 tgt_easyrtcid = e2e_mapping[second_underscore_idx2+1:dot_idx2]

                 if easyrtcid == tgt_easyrtcid:
                    tgt_easyrtcid = src_easyrtcid

                 e2c_mappings = os.listdir(mapping_dir)
                 for e2c_mapping in e2c_mappings:
                    if e2c_mapping.startswith("e2c_") and e2c_mapping.endswith(".mapping"):

                        first_underscore_idx3 = e2c_mapping.find("_");
                        second_underscore_idx3 = e2c_mapping.rfind("_");
                        dot_idx3 = e2c_mapping.rfind(".");

                        tgt_easyrtcid2 = e2c_mapping[first_underscore_idx3 + 1:second_underscore_idx3];
                        cookieid2 = e2c_mapping[second_underscore_idx3+1:dot_idx3]

                        if tgt_easyrtcid == tgt_easyrtcid2:

                            c2c_mapping  = "c2c_" + cookieid  + "_" + cookieid2
                            c2c_mapping2 = "c2c_" + cookieid2 + "_" + cookieid

                            # todo: create a mapping file now if not exist ... and set false value ...


if __name__ == "__main__":
    main(sys.argv)