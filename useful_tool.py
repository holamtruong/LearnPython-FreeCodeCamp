# Create a module in python:
import random

feet_in_mile  = 5280
meter_in_kilometer = 1000
friends = ["Lu", "Su", "Na", "No"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
