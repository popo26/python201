# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread_type, *toppings):
    return f"Your sandwitch will be like this.\n{bread_type} : toppings are {toppings}: then {bread_type}"

your_order = make_sandwich("white bread", "tomato", "salami", "cheese")
print(your_order)



