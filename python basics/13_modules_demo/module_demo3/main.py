# calling the required function alone from another module using import
from validation import validate_and_execute

user_input = ""
while user_input != "exit":
    user_input = input("enter number of days and conversion units\n")
    days_and_units = user_input.split(":")
    day_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    validate_and_execute(day_and_units_dictionary)

