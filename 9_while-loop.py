# while loop
# if u want to do the calculation for multiple values all at once then use while loop
# ie. to execute logic multiple time
calculation_to_units = 24
nameOfUnit = "hours"


def day_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {nameOfUnit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            my_value = day_to_units(user_input_number)
            print(my_value)
        elif user_input_number == 0:
            print("you entered zero")
        else:
            print("you entered a negative number")

    except ValueError:
        print("your input is not valid")


# while True:  #to run program always
# for user to stop the program execution by entering exit
user_input = ""
while user_input != "exit":
    user_input = input("enter number of days\n")
    validate_and_execute()
