# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Add your docstring here.

    This function converts km to mile.

    km parameter:
        km([float]): [length of km]

    Returns:
        [float]: [km converted to mile]

    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
