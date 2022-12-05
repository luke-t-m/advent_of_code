import time
import subprocess
import datetime
import re
import ChatGPT.ChatGPT as ChatGPT


# NOTICE: THIS CODE IS APPALLING. IT'S GETTING A COMPLETE REVAMP (MAYBE). JUST A PROOF OF CONCEPT THAT GOT SECOND PLACE AT ADVENT OF CODE 2022 DAY 4 PART ONE.
# todo: put prompts into correct files
# for ai, generate 
test_mode = False
do_ai = True
do_p2 = False
ai_code_timeout = 1

if test_mode:
    year = "2022"
    day = "3"
    do_wait = True
    file = open("session_cookie")
    session_cookie = file.read()[:-1]
    file.close()
    problem_url = f"https://adventofcode.com/{year}/day/{day}"
    do_p2 = True
else:
    do_input = True
    bad_input_message = "Bad input, try again."
    current_year = int(datetime.datetime.now().strftime("%Y"))
    current_day = int(datetime.datetime.now().strftime("%d"))
    while do_input:
        if do_ai and input("ai part two mode? Y/n: ") == "Y":
            do_p2 = True
        if input("Press enter to use current day for all settings: ") == "":
            #current_year = 2021
            #current_day = 18
            year = str(current_year)
            day = str(current_day)
            do_wait = True
            file = open("session_cookie")
            session_cookie = file.read()[:-1]
            file.close()
            problem_url = f"https://adventofcode.com/{year}/day/{day}"
            break

        while True:
            year = input("year: ")
            if int(year) <= current_year and int(year) >= 2015: break
            print(bad_input_message)
        while True:
            day = input("day: ")
            if int(year) == current_year and int(day) > current_day:
                print(bad_input_message)
                continue
            if int(day) > 0 and int(day) <= 25: break
            print(bad_input_message)
        while True:
            do_wait = input("Should I wait for 5AM before downloading? (Y or n): ")
            if do_wait in "nY" and do_wait != "":
                do_wait = bool("nY".index(do_wait))
                break
            print(bad_input_message)
        while True:
            session_cookie = input("use stored cookie? (Enter or input new cookie portion of header: ")
            if session_cookie == "":
                file = open("session_cookie")
                session_cookie = file.read()[:-1]
                file.close()
                break
            if session_cookie[:16] == "Cookie: session=":
                break
            print(bad_input_message)

        problem_url = f"https://adventofcode.com/{year}/day/{day}"
        print(f"\nurl: {problem_url}\nsession cookie: {session_cookie[:20]}..............{session_cookie[-5:]}\n")
        do_input = input("(n to reinput, enter to proceed): ") == "n"


file = open("chatgpt_bearer_token")
bearer_token = file.read()[:-1]
file.close()

input_url = problem_url + "/input"
contact_info = "User-Agent: https://github.com/luke-t-m/advent_of_code/tree/main/automation therewasanemail@here.once"

# this might break in 2025
year_directory_prefix = str(int(year) - 2015)
if int(year_directory_prefix) >= 10: year_directory_prefix = chr(int(year_directory_prefix)+87)
day_directory_prefix = day
if int(day_directory_prefix) >= 10: day_directory_prefix = chr(int(day_directory_prefix)+87)

year_directory = year_directory_prefix + "_" + year
day_directory = day_directory_prefix + "_day" + day + "_python"
directory = "../" + year_directory + "/" + day_directory

problem_file = day + "_problem"
input_file = day + "_input"
test_file = day + "_test"
own_file = day + ".py"
p1_prompt_file = day + "_p1_prompt"
p2_prompt_file = day + "_p2_prompt"
ai_out_file = day + "_ai_output"

print(f"Attempting to create directory {directory}")
subprocess.run(["mkdir", directory])

today = datetime.date.today()
today_5_o_clock = datetime.datetime.combine(today, datetime.time(5))
time_until = today_5_o_clock - datetime.datetime.now()
if do_wait:
    while True:
        time_until = today_5_o_clock - datetime.datetime.now()
        if time_until <= datetime.timedelta(): break
        if time_until > datetime.timedelta(seconds=10): time.sleep(0.1)
        print(time_until, end = "\r")
print(time_until)

for (file, url) in zip([problem_file, input_file], [problem_url, input_url]):
    print(f"\nDownloading {file}...\n")
    if file not in str(subprocess.check_output(["ls", directory])):
        try: subprocess.check_output(["wget", "--header", session_cookie, "--header", contact_info, "-O", directory + "/" + file, url])
        except:
            print("Something went wrong, probably a 404. Maybe look at your watch? or your internet connection?")
            subprocess.run(["rm", directory + "/" + file])
            print("removed failed download")
    else: print("Already downloaded.")


if test_file not in str(subprocess.check_output(["ls", directory])):
    print("Making test file")
    subprocess.run(["touch", directory + "/" + test_file])
else: print(f"{test_file} already exists.")


if own_file not in str(subprocess.check_output(["ls", directory])):
    print("copying python file template\n")
    file = open("python_template")
    python_template = file.read()
    file.close()
    python_template = python_template.replace("REPLACE_WITH_INPUT_FILE_NAME", input_file)
    python_template = python_template.replace("REPLACE_WITH_TEST_FILE_NAME", test_file)
    subprocess.run(["touch", directory + "/" + own_file])
    file = open(directory + "/" + own_file, "a")
    file.write(python_template)
    file.close()
else: print(f"{own_file} already exists.")

# Should (!) now have all the files needed, and not have messed up anything else

file = open("pre_prompt")
pre_prompt = file.read()
file.close()
pre_prompt = pre_prompt.replace("REPLACE_WITH_INPUT_FILE_NAME", input_file)

file = open(directory + "/" + problem_file)
problem_text = file.read()
file.close()
problem_text = problem_text.split("<main>", maxsplit=1)[1]
problem_text = re.sub("<(.*?)>", "", problem_text)
problem_text = problem_text.split("To begin, get your puzzle input.", maxsplit=1)[0]

prompt = '"""' + pre_prompt + problem_text + '"""'

if p1_prompt_file not in str(subprocess.check_output(["ls", directory])):
    subprocess.run(["touch", directory + "/" + p1_prompt_file])
    file = open(directory + "/" + p1_prompt_file, "w")
    file.write(prompt)
    print("Wrote prompt to file. make edits iff.")
    file.close()
else:
    file = open(directory + "/" + p1_prompt_file)
    prompt = file.read()
    file.close()

print("\nPrompt generated/ read")
if prompt not in open(directory + "/" + own_file).read():
    print("writing prompt to own code file")
    file = open(directory + "/" + own_file, "a")
    file.write("\n\n\n\n\n\n\n" + prompt)
    file.close()
else: print("Prompt already in own code file")

if do_p2:
    print(f"\nDownloading part two {file}...\n")
    file, url = problem_file, problem_url
    subprocess.run(["rm", directory + "/" + file])
    try: subprocess.check_output(["wget", "--header", session_cookie, "--header", contact_info, "-O", directory + "/" + file, url])
    except:
        print("Something went wrong, probably a 404. Maybe look at your watch? or your internet connection?")
        subprocess.run(["rm", directory + "/" + file])
        print("removed failed download")

    # this code is super messy and copy paste, I'm in a rush
    file = open(directory + "/" + problem_file)
    problem_text = file.read()
    file.close()
    problem_text = problem_text.split("<main>", maxsplit=1)[1]
    problem_text = re.sub("<(.*?)>", "", problem_text)
    problem_text = problem_text.split("Although it hasn't changed, you can still get your puzzle input", maxsplit=1)[0]

    prompt = '"""' + pre_prompt + problem_text + '"""'

    print("\nPrompt generated")
    if p2_prompt_file not in str(subprocess.check_output(["ls", directory])):
        subprocess.run(["touch", directory + "/" + p2_prompt_file])
        print("writing prompt to own code file")
        file = open(directory + "/" + p2_prompt_file, "w")
        file.write(prompt)
        file.close()
    else: print("p2 prompt file already exists. Go and edit it!")

    input("Edit p2 prompt file and press enter to continue.")

    file = open(directory + "/" + p2_prompt_file)
    prompt = file.read()
    file.close()

if ai_out_file not in str(subprocess.check_output(["ls", directory])):
    subprocess.run(["touch", directory + "/" + ai_out_file])
else: print("ai output file already exists")

num = 0
while do_ai:
    # IF PART 2 PROMPT FILE EXISTS, GET ON THAT. PRINT TEST FILE OUTPUT AND INPUT OUTPUT TO FILE
    if do_p2: ai_code_file = "z_" + day + f"_ai_p2_{num}.py"
    else: ai_code_file = "z_" + day + f"_ai_p1_{num}.py"
    while ai_code_file in str(subprocess.check_output(["ls", directory])):
        num += 1
        if do_p2: ai_code_file = "z_" + day + f"_ai_p2_{num}.py"
        else: ai_code_file = "z_" + day + f"_ai_p1_{num}.py"
        print("ai code file already exists, increment")


    config = {
        "Authorization": bearer_token
    }

    if 1 == 2: #test_mode:
        response = {}
        response["message"] = """print('its over')"""
    else:
        print("illegal chatgpt usage!!")
        chatbot = ChatGPT.Chatbot(config, conversation_id=None)
        response = chatbot.get_chat_response(prompt)


    if ai_code_file not in str(subprocess.check_output(["ls", directory])):
        subprocess.run(["touch", directory + "/" + ai_code_file])
    else: print("ai code file already exists")

    to_file = response["message"].replace('```', '"""')
    file = open(directory + "/" + ai_code_file, "w")
    file.write(to_file)
    file.close()

    for x in ['"""' + to_file, to_file + '"""', '"""' + to_file + '"""']:
        try: print(subprocess.check_output(["python3", ai_code_file], cwd = directory))
        except:
            file = open(directory + "/" + ai_code_file, "w")
            file.write(x)
            file.close()

    # replace input file name with test file name, run then swap back
    test_result = "NO TEST RESULT"
    input_result = "NO_INPUT_RESULT"
    try:
        print(subprocess.check_output(["python3", ai_code_file], cwd = directory, timeout = ai_code_timeout))
    except:
        print("errors in ai code. Generating again")
        file = open(directory + "/" + ai_out_file, "a")
        try: file.write(f"\n{str(datetime.datetime.now())}, {ai_out_file}, Part two: {do_p2}, test result: {test_result}, input result: {input_result}")
        except: print("couldn't write to ai output file")
        file.close()
        continue
    
    input_result = subprocess.check_output(["python3", ai_code_file], cwd = directory, timeout = ai_code_timeout)

    file = open(directory + "/" + ai_code_file)
    code = file.read()
    file.close
    code = code.replace(input_file, test_file)
    file = open(directory + "/" + ai_code_file, "w")
    file.write(code)
    file.close()

    try:
        print(subprocess.check_output(["python3", ai_code_file], cwd = directory, timeout = ai_code_timeout))
    except:
        print("errors in ai code. Generating again")
        file = open(directory + "/" + ai_code_file)
        code = file.read()
        file.close()
        code = code.replace(test_file, input_file)
        file = open(directory + "/" + ai_code_file, "w")
        file.write(code)
        file.close()
        file = open(directory + "/" + ai_out_file, "a")
        try: file.write(f"\n{str(datetime.datetime.now())}, {ai_out_file}, Part two: {do_p2}, test result: {test_result}, input result: {input_result}")
        except: print("couldn't write to ai output file")
        file.close()
        continue

    test_result = subprocess.check_output(["python3", ai_code_file], cwd = directory, timeout = ai_code_timeout)
    file = open(directory + "/" + ai_code_file)
    code = file.read()
    file.close()
    code = code.replace(test_file, input_file)
    file = open(directory + "/" + ai_code_file, "w")
    file.write(code)
    file.close()

    file = open(directory + "/" + ai_out_file, "a")
    try: file.write(f"\n{str(datetime.datetime.now())}, {ai_code_file}, Part two: {do_p2}, test result: {test_result}, input result: {input_result}")
    except: print("couldn't write to ai output file")
    file.close()
