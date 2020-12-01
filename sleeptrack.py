import datetime
import os
from calendar import monthrange
import random

# Variables and Functions #

current_date = datetime.datetime.now()
day_name = current_date.strftime('%a')
emodays = {'Sun':'', 'Mon':'', 'Tue':'', 'Wed':'', 'Thu':'', 'Fri': '', 'Sat':''}
markov = {
    "1": {"1": 0.9, "2": 0.1, "3": 0, "4": 0, "5": 0},
    "2": {"1": 0.8, "2": 0.2, "3": 0, "4": 0, "5": 0},
    "3": {"1": 0.5, "2": 0.3, "3": 0.2, "4": 0, "5": 0},
    "4": {"1": 0.5, "2": 0.3, "3": 0.1, "4": 0.1, "5": 0},
    "5": {"1": 0.3, "2": 0.3, "3": 0.2, "4": 0.1, "5": 0.1},
    "6": {"1": 0, "2": 0.2, "3": 0.3, "4": 0.3, "5": 0.2},
    "7": {"1": 0, "2": 0, "3": 0.1, "4": 0.5, "5": 0.4},
    "8": {"1": 0, "2": 0, "3": 0.1, "4": 0.6, "5": 0.3},
    "9": {"1": 0, "2": 0, "3": 0.1, "4": 0.6, "5": 0.3},
    "10": {"1": 0, "2": 0, "3": 0.1, "4": 0.6, "5": 0.3},
    }

##############

def date_to_dict(date):
    names = ['year', 'month', 'day']
    date = date.split('-')
    d = dict()
    for ch in range(len(date)):
        if date[ch].startswith('0'):
            date[ch] = date[ch][1]
        d[names[ch]] = int(date[ch])
    return d
date = date_to_dict(str(datetime.date.today()))
days_in_month = monthrange(2020, date['month'])[1]

def check(txt, k):
    with open(txt, 'r') as a:
        for line in a:
            if k in line:
                return True
    return False

def get_filesize(name):
    filesize = os.path.getsize(name)
    return filesize

def emotion(hour, markov):
    probabilities = markov[str(hour)]
    random_num = random.random()
    for k, v in probabilities.items():
        if random_num < v:
            return k
        else:
            random_num -= v

##############


def hello():
    if get_filesize('name.txt') == 0:
        name = input("\nPlease enter your name.\n\n> ").strip()
        with open('name.txt', 'w') as txt:
            txt.write(name)
    with open('name.txt', 'r') as txt:
        for x in txt:
            name = str(x)
            print("\nGood morning, " + name + "! You look great today. Today's date is " 
            + str(datetime.date.today()) + ".\n\nYou can... 'Continue' or  create 'New file' or 'Get Recommendation'. You can quit anytime by entering 'exit'.\n")
        inp = input('> ').strip()
        if inp == 'Continue' or inp == 'continue' or inp == 'c':
            inp = input("\nEnter 'Sleep data' or 'Show graph'\n\n> ").strip()
            if inp == 'Data' or inp == 'data' or inp == 'Sleep data' or inp == 'd':
                data()
            elif inp == 'Show graph' or inp == 'graph' or inp == 'g':
                graph()
        elif inp == 'New file' or inp == 'new' or inp == 'n':
            inp = input("\nAre you sure you wish to start a new file? This will overwrite all memory.\n\n> ").strip()
            if inp == 'Yes' or inp == 'yes' or inp == 'y':
                inp = input("\nAre you really sure?\n\n").strip()
                if inp == 'Yes' or inp == 'yes' or inp == 'y':
                    new_file()
                else:
                    hello()
            else:
                hello()
        elif inp == 'Recommend' or inp == 'rec' or inp == 'r':
            recommend()
        elif inp == 'exit':
            exit()
        else:
            print('\nN/A. Please enter from available commands.')
            hello()

def data():
    print("\nPlease enter time in 24 hour format. (00:00) \n")
    inpsleep = input("When did you fall asleep?\n\n>")
    inpwake = input("\nWhen did you wake up?\n\n>")
    if int(inpsleep.split(':')[0]) < 0 or int(inpsleep.split(':')[0])> 24 or int(inpwake.split(':')[0]) < 0 or int(inpwake.split(':')[0]) > 24:
        print("\nPlease enter a valid time. \n")
        data()
    if int(inpsleep.split(':')[0]) > 12:
        hours = (24 - int(inpsleep.split(':')[0])) + int(inpwake.split(':')[0])
    else:
        hours = int(inpwake.split(':')[0]) - int(inpsleep.split(':')[0])
    inpemotion = int(input("\nOn a scale of 1 - 5, how rested do you feel?\n\n> "))
    emodays[day_name] = (inpemotion * '#')
    
    if day_name == 'Sun' and get_filesize('emodays.txt') != 0:
        if get_filesize('emodays.txt') < 19:
            print("\nSorry, you've already entered data for the day! Try again tomorrow.\n")
            hello()
        with open('emodays.txt', 'w') as txt:
            txt.write(day_name + ' : ' + emodays[day_name] + ' ' + str(hours) + ' hr' + '\n')

    else:
        for k, v in emodays.items():
            if k == day_name and check('emodays.txt', k):
                print("\nSorry, you've already entered data for the day! Try again tomorrow.\n")
                break
            if not check('emodays.txt', k):
                if k == day_name:
                    with open('emodays.txt', 'a') as txt:
                        txt.write(k + ' : ' + v + ' ' + str(hours) + ' hr\n')
                    with open('maindat.txt', 'a') as txt:
                        txt.write(str(hours) + ' ' + str(inpemotion) + '\n')
    hello()

def graph():
    print("\nShowing sleep schedule for this week...\n")
    if get_filesize('emodays.txt') == 0:
        print("No existing files. Return to main menu?\n")
        inp = input("> ").strip()
        if inp == 'Yes' or inp == 'yes' or inp == 'y':
            hello()
        else:
            exit()
    else:
        with open('emodays.txt', 'r') as txt:
            for line in txt:
                print(line)
            inp = input("Return to main menu?\n\n> ").strip()
            if inp == 'Yes' or inp == 'yes' or inp == 'y':
                hello()
            else:
                exit()

def new_file():
    with open('maindat.txt', 'w') as _:
        with open('emodays.txt', 'w') as _:
            with open('name.txt', 'w') as _:
                print("\nFiles deleted!\n")
                inp = input("Return to main menu?\n\n> ").strip()
                if inp == 'Yes' or inp == 'yes' or inp == 'y':
                    hello()
                else:
                    exit()
            
def recommend():
    if get_filesize('maindat.txt') == 0:
        print("\nNo existing files. Return to main menu?\n")
        inp = input("> ").strip()
        if inp == 'Yes' or inp == 'yes' or inp == 'y':
            hello()
        else:
            exit()
    calculations('maindat.txt')

def calculations(file_name):
    opt = 0
    opt_days = 0
    notopt = 0
    notopt_days = 0
    with open(file_name, 'r') as txt:
        for line in txt:
            line = line.split()
            if int(line[1]) > 3:
                opt += int(line[0])
                opt_days += 1
            else:
                notopt += int(line[0])
                notopt_days += 1
        if notopt_days == 0:
            opt = str(round(opt/opt_days))
            print("\nRecommended " + opt + " hours of sleep a day!\n")
            inp = input("Return to main menu?\n\n> ").strip()
            if inp == 'Yes' or inp == 'yes' or inp == 'y':
                hello()
            else:
                exit()
        else:
            opt = str(round(opt/opt_days))
            notopt = str(round(notopt/notopt_days))
            print("\nRecommended " + opt + " hours of sleep a day, no less than " + notopt + "!\n")
            inp = input("Return to main menu?\n\n> ").strip()
            if inp == 'Yes' or inp == 'yes' or inp == 'y':
                hello()
            else:
                exit()

if __name__ == "__main__":
    hello()