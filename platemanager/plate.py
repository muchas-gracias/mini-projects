import argparse
from cmd import Cmd
from faker import Faker
from pathlib import Path
import random
import string
import sys

def random_digit_length():
    return random.randint(1, 4)

def get_digit():
    return random.randint(0, 9)

def get_letter():
    return random.choice(string.ascii_uppercase)

def plate():
    plate = []
    
    for i in range(random_digit_length()): # get set amt of digits
        plate.append(str(get_digit()))
    
    remaining = 8 - len(plate)

    for i in range(remaining): # get set amt of letters
        plate.append(get_letter())

    final_plate = scramble_plates(plate)
    print(final_plate)    

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

    names = set()

    while idx < amt:
        created_first = first()
        created_last = last()
        # plate_number = plate()
        plate()
        
        names.add(created_first)
        names.add(created_last)

        idx += 1

    print(names)

if __name__ == '__main__':
    try:
        Path("plates.txt").write_text("")
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        sys.exit(0)