# calling the required function and variable from another module using import
# from helper import *
# or
from helper import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
    # call variable form helper.py
    user_input = input(user_input_message)
    days_and_units = user_input.split(":")
    day_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    # since the function is called, no need to mention module name before
    validate_and_execute(day_and_units_dictionary)
