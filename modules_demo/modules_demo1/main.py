# importing other module
# import helper as h
# or
import helper

user_input = ""
while user_input != "exit":
    user_input = input("enter number of days and conversion units\n")
    days_and_units = user_input.split(":")
    day_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    # mention the module name before calling the function
    # h.validate_and_execute(day_and_units_dictionary)
    # or
    helper.validate_and_execute(day_and_units_dictionary)
