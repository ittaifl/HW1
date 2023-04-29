#!/usr/bin/env python3
import sys
import os

os.chdir('C:/Users/Antony/Desktop/_tests/Spring_2023_tests/OS/wet1')

TEST_NUMBER = 1 # sys.argv[1]

INPUT_FILE = "./outFiles/test{0}.out".format(TEST_NUMBER)
PROCESSED_FILE = "./processedFiles/test{0}.processed".format(TEST_NUMBER)

smash_pid = -1

def tp_remover(line):
    if line[-1] == "(stopped)" and line[-2] == "secs":
        line[-3] = "__TIME"
        line[-4] = "__PID"
    if line[-1] == "secs":
        line[-2] = "__TIME"
        line[-3] = "__PID"

def spid_fixer(line):
    if len(line) < 4:
        return
    global smash_pid
    if line[0] + " " + line[1] + " " + line[2] == "smash pid is":
        if smash_pid == -1:
            smash_pid = int(line[3])
            line[3] = "__SPID"
        elif smash_pid == int(line[3]):
            line[3] = "__SPID"
        else:
            line[3] = "__BAD_SPID"        

        

with open(INPUT_FILE, 'r') as f_out:
    lines = [line.strip().split() for line in f_out.readlines()]

for line in lines:
    tp_remover(line)
    spid_fixer(line)


with open(PROCESSED_FILE, 'w') as f_proc:
    for line in lines:
        f_proc.write(' '.join(line) + '\n')

