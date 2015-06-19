#!/usr/bin/env python

import sys, os

def runSplitTest(np):
    # np = 2
    # print "------------------------------------------------------------------"
    # print "For processors = ", str(np) + "\n"
    cmdStr = "mpirun -n " + str(np) + " splitTest.py"
    os.system(cmdStr)
    # print "------------------------------------------------------------------\n"

def main():
    """
    Driver for the splitTest.py module. Testing robustness of the list split
    algorithm needed for MPI wrapper class
    """
    runSplitTest(1)
    runSplitTest(2)
    runSplitTest(6)
    runSplitTest(10)
    runSplitTest(11)
    runSplitTest(12)

if __name__ == '__main__':
    main()
