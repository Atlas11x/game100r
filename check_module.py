import sys
import os.path
import random

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


def check_exist_argument_from_user(_listdataclear, _argumentFromUser):
    for i in range(len(_listdataclear)):
        if _argumentFromUser == _listdataclear[i]:
            print("Game over, number exists yet, make new attempt")
            exit()


def check_file_with_random_number():

    file_path = "./random_number.txt"

    if os.path.exists(file_path)==False:
        randomNumber = str(bin(random.randint(0, 100)))
        f = open("random_number.txt", "w+")
        f.write(randomNumber)
        f.close()

        return randomNumber