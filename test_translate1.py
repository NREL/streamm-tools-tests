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

    run_py="python " + toolsPath + "/scripts/translate.py  -v --in_data D1_R2R200_A2_R3_n1_R41n1R41n1R40n1__n5.data     --out_xyz trans_n5.xyz  "

    os.system(run_py)

if __name__ == '__main__':
    main()
