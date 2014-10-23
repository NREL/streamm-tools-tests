#!/usr/bin/env python

import os, sys


def main():
    """
    TRAVIS document
    """
    
    toolsPath = os.getenv("TOOLS_PATH")
    if (toolsPath == None):
        print "TOOLS_PATH is unset. tools repo must be checked out and set this enviroment variable to its location"
        sys.exit(0)

        #run_py="python " + toolsPath + "/scripts/rdf_mda.py  -v -j acc1_D1_R2R200_A2_R3_n1_R41n1R41n1R40n1__n5.json   --in_lammpsxyz  n5.xyz   --fftype_i 'C!'   --fftype_j 'C!'  -o test_rdf "
        #os.system(run_py)

    run_py="python " + toolsPath + "/scripts/rdf_mda.py  -v --in_top PTMA.top   --in_gro EQ_1.gro  -v --in_xtc EQ_1.xtc  --fftype_i 'NN' --fftype_j 'NN'  --frame_step 10  "
    os.system(run_py)

if __name__ == '__main__':
    main()
