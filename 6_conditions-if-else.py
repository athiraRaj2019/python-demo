# if-else conditional loop
calculation_to_units = 24
nameOfUnit = "hours"


# validate the input value is negative/positive using if-else
def day_to_units(num_of_days):
    conditional_check = num_of_days > 0
    print(type(conditional_check))  # will data type of variable 'conditional_check'
    print(conditional_check)  # will print true/false based on input (boolean result)
    # == (equal) , != (not equal), >, >=,< ,<= are called comparison operators
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {nameOfUnit}"
    elif num_of_days == 0:
        return "you entered zero"
    else:
        return "you entered a negative number"


def validate_and_execute():
    #  if-else loop in the input itself.
    # user_input_number = int(user_input)
    if user_input.isdigit():
        my_value = day_to_units(
            int(user_input))  # we can make two lines of code as one by nesting 'int' inside this code.
        print(my_value)
    else:
        print("your input is not valid")


# give inputs like -10 (negative), hello (string), 35.50 (float) it will print "your input is not valid"

user_input = input("enter number of days\n")
validate_and_execute()
