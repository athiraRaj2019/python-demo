# Dictionary data type
# {a:1,b:2,c:3} --> store values in key:value pairs
# dictionary is a collection which does not allow duplicate values
# modify the program as: allow users to provide:
# 1. number of days
# 2.unit to be converted to eg: seconds, minutes, hours etc.


def day_to_units(num_of_days, units):
    if units == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {units}"
    elif units == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {units}"
    elif units == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 *60 *60} {units}"
    else:
        return "invalid input value for units"


def validate_and_execute():
    try:
        user_input_number = int(day_and_units_dictionary["days"])
        if user_input_number > 0:
            my_value = day_to_units(user_input_number, day_and_units_dictionary["units"])
            print(my_value)
        elif user_input_number == 0:
            print("you entered zero")
        else:
            print("you entered a negative number")

    except ValueError:
        print("your input is not valid")


user_input = ""
while user_input != "exit":
    user_input = input("enter number of days and conversion units\n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    day_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(day_and_units_dictionary)
    print(type(day_and_units_dictionary))
    validate_and_execute()
