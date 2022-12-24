#!/usr/bin/env python3
import write_read_file as wrfile
import random
import check_module as check
#get argv from user
import sys


filename = "./database.txt"

check.check_valid_input_data()

argumentFromUser = int(sys.argv[1])
print(f"argumentFromUser: {argumentFromUser}")
check.check_argument_in_range(argumentFromUser)
#--------------------------------------------------------------

randomNumber = check.check_and_generate_random_number()
print(f"random number from computer: {randomNumber}")
wrfile.writeDataInFile(filename, randomNumber)

if argumentFromUser == randomNumber:
    print("You win! Get your 100r!")
else:
    print("Game over. Try again")