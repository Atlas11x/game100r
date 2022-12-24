#!/usr/bin/env python3
import write_read_file as wrfile
import random
#get argv from user
import sys


filename = "./database.txt"

def check_valid_input_data():
    if len(sys.argv) == 1:
        print("WRONG INPUT DATA. Try next with argument")
        exit()


def check_argument_in_range(_argumentFromUser):
    if int(_argumentFromUser) > 100:
        print("Argument is very big. Max 100")
        exit()

    if int(_argumentFromUser) < 0:
        print("Argument is very small. Min 0")
        exit()


def check_exist_argument_from_user(_listdataclear):
    for i in range(len(_listdataclear)):
        if argumentFromUser == _listdataclear[i]:
            print("Game over, number exists yet, make new attempt")
            exit()

check_valid_input_data()

argumentFromUser = sys.argv[1]
print(f"argumentFromUser: {argumentFromUser}")



check_argument_in_range(argumentFromUser)
#--------------------------------------------------------------


databaseContent = wrfile.readDataFromFile(filename)
listdata = []
listdata = databaseContent.split("\n")

listdataclear = []

for i in range(0, len(listdata)-1):
    tmp_list = listdata[i].split("\n")
    listdataclear.append(tmp_list[0])


check_exist_argument_from_user(listdataclear)

randomNumber = random.randint(0, 100)
print(f"random number from computer: {randomNumber}")

if argumentFromUser == randomNumber:
    print("You win! Get your 100r!")
else:
    print("Try again...")
    wrfile.writeDataInFile(filename, argumentFromUser)