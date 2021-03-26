#Functions,Variables,Scope

calculation_to_units = 24
nameOfUnit = "hours"


# define/create  a function
# define function parameter. you can define multiple parameters of different data type:
# int-'num_of_days' and str-'custom_message'
def day_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {nameOfUnit})")
    print(custom_message)


# to get o/p from function you need to call it with function parameter values
day_to_units(20, "hello")
day_to_units(35, "python")
day_to_units(50, "is easy")
day_to_units(110, "to learn")

#variable Scopes in functions: A variable is available from inside the region it is created
#global variables: variables available from within any scope , in our case calculation_to_units, nameOfUnit
#local variable : variables created inside a function can only be used inside that function. In our case num_of_days, custom_message
