# sets
# to avoid duplicate values
# in our case here to avoid duplicate input values like [20,10,20,30], here 20 is repeated.
# list represented using [], where as sets in {}

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
    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()
