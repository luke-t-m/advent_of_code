#!/usr/bin/python3

import time
import datetime
import watchdog.events
import watchdog.observers
import subprocess
import sys

from autom import *



def main():
    now = datetime.datetime.now()
    if len(sys.argv) == 3:
        pos_year, pos_day = sys.argv[1:]
        if not pos_year.isdigit():
            print("bad year. Must be int.")
            exit()
        if not pos_day.isdigit():
            print("bad day. Must be int.")
            exit()
        year = int(pos_year)
        day = int(pos_day)
        if year == now.year and day > now.day:
            print(f"bad day. Expected int between 1 and {now.day}")
            exit()
    elif len(sys.argv) == 1:
        year = now.year
        day = now.day
    else:
        print("bad args. Usage: {sys.argv[0]} OR {sys.argv[0]} year day.")
        exit()
    if not 2015 <= year <= now.year:
        print(f"bad year. Expected int between 2015 and {now.year}.")
        exit()
    if not 1 <= day <= 25:
        print(f"bad day. Expected int between 2015 and {now.year}.")
        exit()
    print(year, day)

    # temp.
    aoc_home = get_env_var()
    input_filename = get_problem_filename(year, day)
    input_filepath = f"{aoc_home}/inputs/{input_filename}"
    solution_dir = f"{aoc_home}/solutions/{year}/{str(day).zfill(2)}/first_attempt"
    solution_file = f"{solution_dir}/solution.py"
    start_watch(solution_file, input_filepath)


if __name__ == "__main__":
    main()