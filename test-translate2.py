#!/usr/bin/env python

import os, sys

toolsPath = os.getenv("TOOLS_PATH")
if (toolsPath == None):
    print "TOOLS_PATH is unset. tools repo must be checked out and set this enviroment variable to its location"
    sys.exit(0)

run_py="python " + toolsPath + "/scripts/translate.py  -v --in_data qd.data  --out_data test2.data     --out_xyz test2.xyz  "
os.system(run_py)

run_py="python " + toolsPath + "/scripts/translate.py  -v --in_gro SOL.gro --in_top SOL.top   --out_data SOL.data     --out_xyz SOL.xyz  "
os.system(run_py)
