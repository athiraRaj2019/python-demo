def day_to_units(num_of_days, units):
    if units == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {units}"
    elif units == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {units}"
    elif units == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {units}"
    else:
        return "invalid input value for units"
