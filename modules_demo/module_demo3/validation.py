from days_to_units import day_to_units

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

