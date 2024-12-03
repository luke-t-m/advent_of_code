#!/usr/bin/python3

import time
import datetime
import watchdog.events
import watchdog.observers
import subprocess
import sys
import os

AOC_ENV_VAR = "AOC_HOME"
SESSION_COOKIE_FILENAME = "session_cookie"


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


def get_problem_filename(year, day):
    return str(year) + str(day).zfill(2)


def get_env_var():
    if AOC_ENV_VAR not in os.environ:
        print(f"ERROR: Could not find {AOC_ENV_VAR} in environment variables.")
        exit()

    return os.environ[AOC_ENV_VAR]


def get_session_cookie():
    aoc_home = get_env_var()
    session_cookie_filepath = f"{aoc_home}/{SESSION_COOKIE_FILENAME}"

    return readFileOrError(session_cookie_filepath)


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


def start_watch(solution_file, input_file):
    print(f"\n\nBeginning watch over {solution_file}.")

    raw_input = readFileOrError(input_file)

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

