def day_to_units(num_of_days, units):
    if units == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {units}"
    elif units == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {units}"
    elif units == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {units}"
    else:
        return "invalid input value for units"


def validate_and_execute(day_and_units_dictionary):
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


user_input_message = "enter number of days and conversion units\n"
