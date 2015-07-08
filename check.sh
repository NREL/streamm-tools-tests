#
# Help message
#
usage() {
    echo " "
    echo "Usage: check.sh [arg]"
    echo "    arg -- new                 : Runs tests and copies output to results directory"
    echo "        -- all                 : Runs all tests and compares to files in results directory"
    echo "        -- clean               : Remove auxillary files generated from running tests"
    echo "        -- 'test-name'         : Run compare for 'test-name'"
    echo "        -- replace 'test-name' : Runs test and copies output to results directory"
    echo " "
    echo " "
    echo "To add a SERIAL test:"
    echo "   1. create test with name test-*.py "
    echo "      Note: test_*.py is assumed to print results to screen \n"
    echo "   2. do 'check.sh compare' \n"
    echo "   3. double check that 'check.sh compare' gives no errors \n"
    echo "   4. do 'check.sh new' to put new results in /tools/tests/results \n"
    echo "   5. make sure to git add/commit/push new test and new results \n"
    echo " "
    echo " "
    echo "To add a PARALLEL (np = 2) test:"
    echo "   1. create test with name test_n2_*.py "
    echo "      Note: test_*.py is assumed to print results to screen \n"
    echo "   2. Repeat steps 2-5 for serial"
    echo " "
    echo " "
    echo "Note: if parallel np > 2 tests needed script will need to be edited"
    echo " "
}


#
# Runs test comparison and checks with results in ./results and assumes
# form of the file testName.txt
# Ignores lines with expressions matched in IGNORE_OPTION
#
# Checks length of the diff status file and returns passed if 0 and
# failed if > 0
#
compareTest() {

    IGNORE_OPTIONS='-I Found* -I Date* -I Derived* -I Finished* -I Computation*'
    testName=$1
    runCmd=$2

    $runCmd ./$testName > tmp
    diff $IGNORE_OPTIONS tmp results/$testName.txt > $testName.stat
    diffLength=`wc -l $testName.stat | awk '{print $1}'`
    rm -rf tmp

    # Calculate length of status message
    TOTAL_COLUMNS=60
    lineLength=`echo "Running $runCmd $testName: " |wc -c`
    COLUMNS=$((TOTAL_COLUMNS-lineLength))

    # Status message
    if [ $diffLength == '0' ]; then
	printf "Running $runCmd $testName: %${COLUMNS}s\n" "Passed"
    else
        echo   "-----------------------------------------------------------"
	printf "Running $runCmd $testName: %${COLUMNS}s\n"          "FAILED"
	echo   "        Check $testName.stat for details                   "
        echo   "-----------------------------------------------------------"
    fi
}


#
# Checks new results into repo
#
newTest() {

    testName=$1
    runCmd=$2
    echo "--------- Copying results for $testName ---------"
    $runCmd ./$testName > results/$testName.txt
    echo "Remember to commit/push new results "
    echo "-----------------------------------------------------"
    echo " "
}


#
# Check if TOOLS_PATH is set
#
if [ ! -n "${TOOLS_PATH+1}" ]; then
    echo " "
    echo "---------------------------------------------------------------"
    echo "TOOLS_PATH is unset. Set location of 'tools' repo to this var"
    echo " "
    echo " eg: TOOLS_PATH='path-to-tools'/tools"
    echo "     then "
    echo "     export TOOLS_PATH"
    echo "---------------------------------------------------------------"
    echo " "
    exit
fi


#
# Main functions
#
if [ $# == 0 ]; then
    usage

elif [ $1 == "new" ]; then

    echo " "
    echo "Checking in new results for python test files"
    echo "Looking for tests named 'test_*.py'  "
    echo " "

    echo "Proceed [y]yes [n]no"
    read -e ans
    if [ $ans == "y" ]; then
	echo " "
    else
	echo " "; exit
    fi

    # Serial test
    testNames=`ls -1 test_*.py |grep -v test_n2 |grep -v test_nX`
    runCmd="python"
    for testName in $testNames; do
	newTest $testName $runCmd
    done

    # Parallel test (np = 2)
    testNames=`ls -1 test_n2_*.py`
    for testName in $testNames; do
	newTest $testName ' mpirun -n 2'
    done


elif [ $1 == "all" ]; then

    echo " "
    echo "Comparing results against python test files"
    echo "Looking for tests named 'test_*.py'  "
    echo " " 

    # Serial test
    testNames=`ls -1 test_*.py |grep -v test_n2 |grep -v test_nX`
    runCmd="python "
    for testName in $testNames; do
	compareTest $testName $runCmd
    done

    # Parallel test (np = 2)
    testNames=`ls -1 test_n2_*.py`
    for testName in $testNames; do
	compareTest $testName 'mpirun -n 2'
    done

    # Parallel test (series of parallel runs that are calling mpirun internally)
    testNames=`ls -1 test_nX_*.py`
    for testName in $testNames; do
	compareTest $testName
    done

    echo " "


elif [ $1 == "replace" ]; then

    testName=$2

    echo " "
    echo "Checking in new results for $testName"
    echo " "

    echo "Proceed [y]yes [n]no"
    read -e ans
    if [ $ans == "y" ]; then
	echo " "
    else
	echo " "; exit
    fi

    if [[ $testName == *n2* ]]; then
        # Pick out job to run on 2 procs
	newTest $testName ' mpirun -n 2'
    else
        # Serial job
	newTest $testName " "
    fi


elif [ $1 == "clean" ]; then

    echo " "
    echo "Removing auxillary files generated during tests"
    echo " "

    rm -rf *.pkl qd*dat stats.txt qd.data trans.dat trans.log
    rm -rf test_rdf.log test_rdf.dat test*.pyc
    rm -rf replicate.gro replicate.json replicate.log replicate.xmol
    rm -rf test*.py.stat
    rm -rf *.pkl qd.data*
    rm -rf test-strucAddBig-timing.dat


else

    # Run single test
    echo " "
    testName=$1

    if test -f $testName; then

	if [[ $testName == *n2* ]]; then
            # Pick out job to run on 2 procs
	    compareTest $testName 'mpirun -n 2'
	else
            # Serial/other jobs
	    compareTest $testName ''
	fi

    else
	echo "Test name does not exist"
    fi


fi
