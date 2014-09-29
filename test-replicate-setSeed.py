#!/usr/bin/env python

import os, sys

toolsPath = os.getenv("TOOLS_PATH")
if (toolsPath == None):
    print "TOOLS_PATH is unset. tools repo must be checked out and set this enviroment variable to its location"
    sys.exit(0)

run_py="python " + toolsPath + "/scripts/replicate.py --fixed_rnd_seed --gro SOL.gro --top SOL.top   --sol_gro SOL.gro   --sol_top SOL.top   --den_target 0.1  --atoms_target 200    --perc_sol 50 -v "
print run_py
os.system(run_py)


