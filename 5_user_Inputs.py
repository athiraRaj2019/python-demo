# user inputs, function return, casting
calculation_to_units = 24
nameOfUnit = "hours"


# define/create  a function
# define function parameter. you can define multiple parameters of different data type:
# int-'num_of_days' and str-'custom_message'
# function has to return a value
def day_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {nameOfUnit}"


# to get o/p from function you need to call it with function parameter values
user_input = input("enter number of days\n")
# since input takes values as integers we need to cast them as integer first before using in function.
user_input_number = int(user_input)
# print the result returned by function
my_value = day_to_units(user_input_number)
print(my_value)
