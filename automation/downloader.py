#!/usr/bin/python3

import time
import datetime
import os
import requests
import watchdog.events
import watchdog.observers
import subprocess
import pathlib




#quick and hacky downloader script started at 0100 dec 01.

# TODOING:
# load variables and shit from environ and gitignored files.
# check for missing inputs and download them.
# wait till its 6 o clock, then try and download the input and store it at filepath.
# filewatcher on solver script. When file changes, try to run in thread and display most recent run in terminal window.


aoc_env_var = "AOC_HOME"
session_cookie_filename = "session_cookie"
template_filename = "solution.py"


def get_problem_filename(year, day):
  return str(year)[2:] + str(day).zfill(2)

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


def fileExists(filename):
  try:
    with open(filename) as file:
      file.read()
    return True
  except:
    return False

def readFileOrError(filename):
  try:
    with open(filename) as file:
      return file.read().strip()
  except:
    print(f"ERROR: file not found {filename}.")
    exit()


class FileEventHandler(watchdog.events.FileSystemEventHandler):
    def __init__(self, file, input):
      self.file = file
      self.input = input
      self.last_bothered = datetime.datetime.now()
      self.process = subprocess.Popen([self.file, self.input])

    def on_any_event(self, event: watchdog.events.FileSystemEvent) -> None:
          if event.event_type == "modified":
            bothered = datetime.datetime.now()
            if (bothered - self.last_bothered).total_seconds() > 1:
              time.sleep(0.1)
              self.last_bothered = bothered
              self.process.kill()
              print("\n\n\n")
              self.process = subprocess.Popen([self.file, self.input])



# Get session cookie from file.

if aoc_env_var not in os.environ:
  print(f"ERROR: Could not find {aoc_env_var} in environment variables.")
  exit()

aoc_home = os.environ[aoc_env_var]
session_cookie_filepath = f"{aoc_home}/{session_cookie_filename}"

session_cookie = readFileOrError(session_cookie_filepath)


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
solution_file = f"{solution_dir}/{template_filename}"
template_filepath = f"{aoc_home}/templates/{template_filename}"

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

print(f"\n\nBeginning watch over {solution_file}.")

input_filename = get_problem_filename(release.year, release.day)
input_filepath = f"{aoc_home}/inputs/{input_filename}"
raw_input = readFileOrError(input_filepath)

# Begin watching solution file.

event_handler = FileEventHandler(solution_file, raw_input)
observer = watchdog.observers.Observer()
observer.schedule(event_handler, solution_file)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()