import argparse
from cmd import Cmd
from faker import Faker
from pathlib import Path
import random
import string
import sys

from fileparsing import FileParsing

PLATES = "plates.txt"

def random_digit_length():
    return random.randint(1, 4)

def get_digit():
    return random.randint(0, 9)

def get_letter():
    return random.choice(string.ascii_uppercase)

def plate() -> str:
    plate = []
    
    for i in range(random_digit_length()): # get set amt of digits
        plate.append(str(get_digit()))
    
    remaining = 8 - len(plate)

    for i in range(remaining): # get set amt of letters
        plate.append(get_letter())

    final_plate = scramble_plates(plate)

    return final_plate   

def scramble_plates(plate: list) -> str:
    string = ""
    random.shuffle(plate)
    for each in plate:
        string = string + each
    return string

    
def first():
    fake = Faker()
    first = fake.first_name()

    return first

def last():
    fake = Faker()
    last = fake.last_name()
    return last

def main():
    idx = 0

    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-i', "--amount", type=int, required=True, help="Amount of License Plates")
    args = parser.parse_args()

    amt = args.amount

    while idx < amt:
        created_first = first()
        created_last = last()
        plate_number = plate()

        parser = FileParsing(created_first, created_last, plate_number)

        if parser.is_in_file(False):
            continue
        
        if parser.is_in_file(True):
            continue

        parser.add_to_file() # add row of info to file

        idx += 1

if __name__ == '__main__':
    try:
        letter_list = list(string.ascii_lowercase)
        for each in letter_list:
            parser = FileParsing(last=each)
            parser.create_files()
 
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        sys.exit(0)