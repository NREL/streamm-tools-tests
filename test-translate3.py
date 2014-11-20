#!/usr/bin/env python

import os, sys

toolsPath = os.getenv("TOOLS_PATH")
if (toolsPath == None):
    print "TOOLS_PATH is unset. tools repo must be checked out and set this enviroment variable to its location"
    sys.exit(0)

run_py="python " + toolsPath + "/scripts/translate.py  --in_json acc1_D1_R2R200_A31_R4_n1_R41n1R41n1R40n1__n5x100k.json --in_data prod1.data --out_xyz prod1.xyz   "
os.system(run_py)
