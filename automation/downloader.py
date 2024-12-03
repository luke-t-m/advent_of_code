#!/usr/bin/python3

import time
import datetime
import os
import requests
import subprocess
import pathlib
from autom import *

TEMPLATE_FILENAME = "solution.py"


def download_input(year, day, session, aoc_home, max_trys=1):
  input_filename = get_problem_filename(year, day)
  input_filepath = f"{aoc_home}/inputs/{input_filename}"
  if fileExists(input_filepath):
    return False
  else:
    trys = 0
    while trys < max_trys:
      response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session})
      if response.status_code == 200:
        with open(input_filepath, "wb") as file:
          file.write(response.content)
        print(f"Downloaded input for {year} day {day}.")
        return True
      else:
        trys += 1
        print(f"Failed to download input for {year} day {day} with error code {response.status_code}. Retrying...")
        time.sleep(1)
  return False

def respectfully_download_input(year, day, session, aoc_home, to_sleep=15):
  i = download_input(year, day, session, aoc_home)
  if i:
    time.sleep(to_sleep)
  return i




# Get session cookie from file.

aoc_home = get_env_var()
session_cookie = get_session_cookie()



# Current time and when the problem will release.
now = datetime.datetime.now(datetime.timezone.utc)
release = now.replace(hour=5, minute=0, second=0, microsecond=0)
if now.hour > 4:
  release = release.replace(day=now.day+1)
if now.month != 12:
  release = release.replace(month=12, day=1)
elif now.day > 25:
  release = release.replace(day=1, year=now.year+1)


# Check/ make setup for problem.
solution_dir = f"{aoc_home}/solutions/{release.year}/{str(release.day).zfill(2)}/first_attempt"
solution_file = f"{solution_dir}/{TEMPLATE_FILENAME}"
template_filepath = f"{aoc_home}/templates/{TEMPLATE_FILENAME}"

template_file = readFileOrError(template_filepath)

pathlib.Path(solution_dir).mkdir(parents=True, exist_ok=True)
if not fileExists(solution_file):
  with open(solution_file, "w") as file:
    file.write(template_file)
  print(f"Created file for solution {solution_file} from {template_filepath}")

subprocess.run(["chmod", "+x", solution_file])



# Fetch missing previous inputs (if we have time before release).

to_sleep = 1
total_inputs = (now.year - 2015) * 25 + now.day
local_inputs = len(os.listdir(f"{aoc_home}/inputs"))
total_sleep = (total_inputs - local_inputs) * to_sleep

if (release - now).total_seconds() > total_sleep:
  print(f"Downloading missing inputs. Will take {total_sleep} seconds.")
  for year in range(2015, now.year):
    for day in range(1, 26):
      respectfully_download_input(year, day, session_cookie, aoc_home, to_sleep)

  year = now.year
  if now.month == 12:
    for day in range(1, min(release.day, 26)):
      respectfully_download_input(year, day, session_cookie, aoc_home, to_sleep)



# Sleep till 0500 UTC and download.

while now < release:
  print(f"Problem releasing in {release - now}. Sleeping...", end='\r')
  now = datetime.datetime.now(datetime.timezone.utc)
  time.sleep(0.5)

download_input(release.year, release.day, session_cookie, aoc_home, max_trys=5)

input_filename = get_problem_filename(release.year, release.day)
input_filepath = f"{aoc_home}/inputs/{input_filename}"
start_watch(solution_file, input_filepath)
