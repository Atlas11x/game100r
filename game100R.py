#!/usr/bin/env python3
import write_read_file as wrfile
import random
import check_module as check
#get argv from user
import sys


filename = "./database.txt"


check.check_valid_input_data()

argumentFromUser = sys.argv[1]
print(f"argumentFromUser: {argumentFromUser}")



check.check_argument_in_range(argumentFromUser)
#--------------------------------------------------------------


databaseContent = wrfile.readDataFromFile(filename)
listdata = []
listdata = databaseContent.split("\n")

listdataclear = []

for i in range(0, len(listdata)-1):
    tmp_list = listdata[i].split("\n")
    listdataclear.append(tmp_list[0])


check.check_exist_argument_from_user(listdataclear, argumentFromUser)
check.check_file_with_random_number()

decodeFromStr = wrfile.readDataFromFile("random_number.txt")[2:]
computerInt = int(decodeFromStr, 2)

if int(argumentFromUser) == computerInt:
    print("You win! Get your 100r!")
else:
    print("Try again...")
    wrfile.writeDataInFile(filename, argumentFromUser)
