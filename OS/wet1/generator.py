#!/usr/bin/env python3

import os
import random
import string

os.chdir('C:/Users/Antony/Desktop/_tests/Spring_2023_tests/OS/wet1')

TEST_AMOUNT = 3
LINES_PER_TEST = 100

END_LINE = "\n"
FILE_PATH_LIST = ["./test_path", "./double/test_path", "../path_with_back", "./very/long/path/test"] #add more
DIR_PATH_LIST = ["./test_path", "./double/test_path", "../path_with_back", "./very/long/path/test", "-", ".."]

# random space string
def rss():
    space_amount = random.randint(0, 10)
    space_amount -= 5
    if space_amount < 0:
        space_amount = 1
    spaces_str = " " * space_amount

    return spaces_str

def rs():
    if random.randint(0, 10) != 0:
        return ""
    # Define the set of characters to choose from
    chars = string.ascii_letters + string.digits

    # Generate a list of random characters of the desired length
    rand_chars = [random.choice(chars) for _ in range(5)]

    # Concatenate the characters into a string
    rand_string = "".join(rand_chars)

    return rand_string

# &
def aa():
    ampersand = "&" * random.randint(0, 1)
    return ampersand


def gen_chprompt():
    name_list = ["test_destroyer7000", "Donald_Trump", "Not_a_Bot", "Jimmy_Wizard",
                 "EinTropit", "shell", "Sonic_The_Hedgehog", "Ori_ben_zur_the_spy", ""]
    return rss() + "chprompt" + rss() + name_list[random.randint(0, len(name_list) - 1)] + rss()  + aa() + rss() + END_LINE


def gen_showpid():
    return rss() + "showpid" + rss() + rs() + rss() + aa() + rss() + aa() + rss() + END_LINE


def gen_pwd():
    return rss() + "pwd" + rss() + rs() + rss() + aa() + rss() + aa() + rss() + END_LINE


def gen_cd():
    return rss() + "cd" + rss() + DIR_PATH_LIST[random.randint(0, len(DIR_PATH_LIST) - 1)]\
           + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_jobs():
    return rss() + "jobs" + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_fg():
    if random.randint(0, 3) == 0:
        return rss() + "fg" + rss() + aa() + rss() + END_LINE
    return rss() + "fg" + rss() + str(random.randint(1,10)) + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_bg():
    if random.randint(0, 3) == 0:
        return rss() + "bg" + rss() + aa() + rss() + END_LINE
    return rss() + "bg" + rss() + str(random.randint(1,10)) + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_quit():
    return rss() + "quit" + rss() + "kill" * random.randint(0,1) + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_kill():
    signal_list = ["9", "18", "19", "20", "supersecretword", "50", ]
    if random.randint(0,3) == 0:
        minus_sign = 0
    else:
        minus_sign = 1

    return rss() + "kill" + rss() + "-" * minus_sign + signal_list[random.randint(0, len(signal_list) - 1)] \
           + rss() + rs() + rss() + str(random.randint(1, 10)) + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_setcore():
    core_list = ["0", "1", "1525", "boi" ]
    return rss() + "setcore" + rss() + str(random.randint(1, 10)) + rss() \
           + core_list[random.randint(0, len(core_list) - 1)] + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_getfiletype():
    return rss() + "getfiletype" + rss() + FILE_PATH_LIST[random.randint(0, len(FILE_PATH_LIST) - 1)]\
           + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_chmod():
    mode = str(random.randint(0, 7)) * 3
    return rss() + "chmod" + rss() + mode + rss() + FILE_PATH_LIST[random.randint(0, len(FILE_PATH_LIST) - 1)]\
           + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_timeout():
    _random_command = random.choice(command_list)
    while _random_command == gen_timeout or _random_command == gen_ctrl_Z() or _random_command == gen_ctrl_C :
        _random_command = random.choice(command_list)
    return rss() + "timeout" + rss() + str(random.randint(1, 30)) + rss() + _random_command() + rss() + aa() + rss() + END_LINE


def gen_ctrl_Z():
    return "^Z" + END_LINE


def gen_ctrl_C():
    return "^C" + END_LINE


def gen_sleep():
    return rss() + "sleep" + rss() + str(random.randint(1, 100000))\
           + rss() + rs() + rss() + aa() + rss() + END_LINE


def gen_ls():
    return rss() + "ls" + rss() + rs() + rss() + aa() + rss() + aa() + rss() + END_LINE


def gen_whoami():
    return rss() + "whoami" + rss() + rs() + rss() + aa() + rss() + aa() + rss() + END_LINE

def gen_cat():
    return rss() + "cat" + rss() + FILE_PATH_LIST[random.randint(0, len(FILE_PATH_LIST) - 1)]\
           + rss() + rs() + rss() + aa() + rss() + END_LINE


"""
consider adding:
grep
touch
rm

execute a file

>>
>
|
|&

"""

command_list = [gen_chprompt, gen_showpid, gen_pwd, gen_jobs, gen_fg, gen_bg, gen_quit, gen_kill, gen_setcore, gen_getfiletype, gen_chmod, gen_timeout, gen_ctrl_Z, gen_ctrl_C, gen_sleep, gen_ls, gen_cat, gen_whoami ]

for i in range(0, TEST_AMOUNT):
    f_test = open(f'./inFiles/test{i}.in', 'w')
    for j in range(0, LINES_PER_TEST):
        random_command = random.choice(command_list)
        f_test.write(random_command())
    f_test.close()
