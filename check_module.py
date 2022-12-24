import sys
import os.path
import random
import write_read_file as wr

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


def check_and_generate_random_number():
    randomInt = random.randint(0, 100)

    data = wr.readDataFromFile(filename)

    if len(data) == 0:
        randomInt = random.randint(0, 100)
        return randomInt
    new_data = data.split("\n")
    randomInt = random.randint(0, 100)

    while True:
        test = True

        for i in range(len(new_data)):

            if str(randomInt) == new_data[i]:
                test = False
                break

        if test == True:
            return randomInt