#!/usr/bin/env python3
import sys

TEST_NUMBER = sys.argv[1]

INPUT_FILE = "test{TEST_NUMBER}.out"
PROCESSED_FILE = "test{TEST_NUMBER}.processed"

with open(INPUT_FILE, 'r') as f_out:
    lines = [line.strip().split() for line in f_out.readlines()]





with open(PROCESSED_FILE, 'w') as f_proc:
    for line in lines:
        f_proc.write(' '.join(line) + '\n')
