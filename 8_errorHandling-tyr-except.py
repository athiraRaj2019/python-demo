# try-except for error handling
calculation_to_units = 24
nameOfUnit = "hours"


def day_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {nameOfUnit}"


# generally try-except used for situations where u cannot validate using if-else.
# Here we have replaced the conditional if-else using try-except
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
            # we know our error here is value error hence mentioned that.
            # You can simply use except:to catch any kind of possible errors
            # if u use except alone , then it will give a warning(ignore it)
    # except:
    except ValueError:
        print("your input is not valid")


user_input = input("enter number of days\n")
validate_and_execute()
