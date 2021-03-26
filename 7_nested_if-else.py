# nested if-else conditional loop
calculation_to_units = 24
nameOfUnit = "hours"


# instead of validating 2 times in 2 different functions we can do it
# all together using nested-if so that code looks a bit better.
def day_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {nameOfUnit}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            my_value = day_to_units(user_input_number)
            print(my_value)
        elif user_input_number == 0:
            print("you entered zero")
    else:
        print("your input is not valid")


user_input = input("enter number of days\n")
validate_and_execute()
