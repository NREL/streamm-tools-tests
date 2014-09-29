#!/usr/bin/env python

import os, sys

toolsPath = os.getenv("TOOLS_PATH")
if (toolsPath == None):
    print "TOOLS_PATH is unset. tools repo must be checked out and set this enviroment variable to its location"
    sys.exit(0)

run_py="python " + toolsPath + "/scripts/rdf.py  -v  --in_data D1_R2R200_A2_R3_n1_R41n1R41n1R40n1__n5.data    --in_lammpsxyz  n5.xyz   --symb_i 'C'   --symb_j 'C'  -o test_rdf "
os.system(run_py)

