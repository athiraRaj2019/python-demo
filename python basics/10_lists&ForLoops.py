# lists and for loops
# list-stores multiple items in a single variable. each items can b of different data type
# here we can pass a list of user_inputs

calculation_to_units = 24
nameOfUnit = "hours"


def day_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {nameOfUnit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            my_value = day_to_units(user_input_number)
            print(my_value)
        elif user_input_number == 0:
            print("you entered zero")
        else:
            print("you entered a negative number")

    except ValueError:
        print("your input is not valid")


user_input = ""
while user_input != "exit":
    user_input = input("enter comma separated input and I will convert it to hours\n")
    # split function in python will always return a list of input values
    print(type(user_input.split(", ")))
    print(user_input.split(", "))
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
