#!/usr/bin/python

import os, sys

def main(argv):

    mapping_dir = argv[1];
    print 'mapping directory  : ', mapping_dir;

    c2e_mappings = os.listdir(mapping_dir)
    for c2e_mapping in c2e_mappings:
       if c2e_mapping.startswith("c2e_") and c2e_mapping.endswith(".mapping"):

          c2e_1st_underscore_idx = c2e_mapping.find("_");
          c2e_2nd_underscore_idx = c2e_mapping.rfind("_");
          c2e_dot_idx            = c2e_mapping.rfind(".");

          c2e_src_cookieid  = c2e_mapping[c2e_1st_underscore_idx+1:c2e_2nd_underscore_idx];
          c2e_src_easyrtcid = c2e_mapping[c2e_2nd_underscore_idx+1:c2e_dot_idx]

          e2e_mappings = os.listdir(mapping_dir)
          for e2e_mapping in e2e_mappings:
             if e2e_mapping.startswith("e2e_") and e2e_mapping.endswith(".mapping"):

                 e2e_1st_underscore_idx = e2e_mapping.find("_");
                 e2e_2nd_underscore_idx = e2e_mapping.rfind("_");
                 e2e_dot_idx            = e2e_mapping.rfind(".");

                 e2e_src_easyrtcid = e2e_mapping[e2e_1st_underscore_idx+1:e2e_2nd_underscore_idx];
                 e2e_tgt_easyrtcid = e2e_mapping[e2e_2nd_underscore_idx+1:e2e_dot_idx];

                 if c2e_src_easyrtcid == e2e_src_easyrtcid:

                    e2c_mappings = os.listdir(mapping_dir)
                    for e2c_mapping in e2c_mappings:
                        if e2c_mapping.startswith("e2c_") and e2c_mapping.endswith(".mapping"):

                            e2c_1st_underscore_idx = e2c_mapping.find("_");
                            e2c_2nd_underscore_idx = e2c_mapping.rfind("_");
                            e2c_dot_idx            = e2c_mapping.rfind(".");

                            e2c_tgt_cookieid  = e2c_mapping[e2c_1st_underscore_idx+1:e2c_2nd_underscore_idx];
                            e2c_tgt_easyrtcid = e2c_mapping[e2c_2nd_underscore_idx+1:e2c_dot_idx]

                            if e2e_tgt_easyrtcid == e2c_tgt_easyrtcid:

                                c2c_src_tgt_mapping = "c2c_" + c2e_src_cookieid + "_" + e2c_tgt_cookieid + ".mapping"
                                c2c_tgt_src_mapping = "c2c_" + e2c_tgt_cookieid + "_" + c2e_src_cookieid + ".mapping"

                                createMappingFile(mapping_dir + c2c_src_tgt_mapping)
                                createMappingFile(mapping_dir + c2c_tgt_src_mapping)

def createMappingFile(c2c_mapping_file_path):
    if not os.path.exists(c2c_mapping_file_path):
        with open(c2c_mapping_file_path, 'w') as f:
            f.write("false")

if __name__ == "__main__":
    main(sys.argv)