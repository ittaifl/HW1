#!/bin/bash

MAX_TEST=100


RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

EXIT_STATUS=0
FAILED_AMOUNT=0

if [ -z "$1" ]; then
	TEMP=0
else
	TEMP=$1
fi

if (( "$TEMP" >= 1 && "$TEMP" <= $MAX_TEST )); then
	TEST_BEGIN=$1
	TEST_END=$1
else
	TEST_BEGIN=1
	TEST_END=$MAX_TEST
fi


for ((i=$TEST_BEGIN; i<=$TEST_END; i++)); do 

	g++ -std=c++11 -g -Wall -Werror -pedantic-errors -ggdb3 -DNDEBUG ./files/*.cpp -o smash
	./smash < ./inFiles/test${i}.in > ./outFiles/test${i}.out
	python update.py ${i}

	if cmp -s "/processedFiles/test${i}.processed" "/comareFiles/test${i}.compare"; then 
		echo -e "test${i}: ${GREEN}PASS${NC}"
	else
		echo -e "test${i}: ${RED}FAIL${NC}"
		((STATUS++))
	fi
done

if [ $STATUS == 0 ]; then
	echo -e "status: all tests ${GREEN}PASSED${NC}"
else
	echo -e "status: ${i} tests ${RED}FAILED${NC}"
	EXIT_STATUS=1
fi


echo -e "Terminating runner"
exit ${EXIT_STATUS}