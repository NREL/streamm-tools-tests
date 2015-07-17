#!/usr/bin/env python
"""
S. Sides  (NREL)
Script to enable converting a test*.py file to an ipython
version and an associated *.rst file for documentation
"""

import os, sys

try:
    import IPython.nbformat.current as nbf
except:
    print "Error: IPython module not found, check PYTHONPATH and ipython installation"
    sys.exit(3)

try:
    from optparse import OptionParser
except:
    print "Error: optparse not found, 'PYTHONPATH'"
    sys.exit(3)


#####################################################################################################
# Command line option parse

parser = OptionParser()
usage = """

%prog [options]

     Converts python file to ipython notebook.

     ************************************************************************************
     Instructions for creating documentation suitable for the STREAMM project:
     ************************************************************************************
       1. Use this script to convert test_XXXX.py ---> test_XXXX.ipynb
       2. Use ipython notebook test_XXXX.ipynb to open and edit notebook, includes:
          * adding/editing comments
          * removing code out of main()
          * spliting cells to facilitate adding comments
       3. Save notebook
       4. Rename test_XXXX.ipynb to example_XXXX.ipynb and move to tools/docs/source
       5. Use 'ipython nbconvert --to rst example_XXXX.ipynb' to create example_XXXX.rst file
       6. Add .rst file to docs
       7. Add download line for ipynb file to example_XXXX.rst file
"""

parser.set_usage(usage)

parser.add_option("--testname",
                  dest="testname",
                  type="string",
                  help="Name of test_xxxx python file to convert (without the .py extension) \n")

# Acessing options
(options,args) = parser.parse_args()
testname       = options.testname

# Check if options set
if (testname==None):
    options_set=False
else:
    # Check top direcotry which must be present
    options_set=True
    print " "
    print "Test name ", testname, " found"
    print " "
    if ( not os.path.exists(testname + '.py') ):
        print "Python test file (specify with --testname) doesn't exist \n"
        sys.exit(1)
#####################################################################################################


##########################
# main section
##########################

if (options_set):

    # Convert .py ---> .ipynb
    nb = nbf.read(open(testname + '.py',    'r'), 'py')
    nbf.write(nb, open(testname + '.ipynb', 'w'), 'ipynb')
    print "File ", testname + '.ipynb', " written"


# If no options, print help message
else:
    parser.print_help()
