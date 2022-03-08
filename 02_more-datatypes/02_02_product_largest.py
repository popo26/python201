# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

random_list = randlist
print(random_list)

highest_price = max(random_list)
print(highest_price)

sum_of_all_numbers = sum(random_list)
print(sum_of_all_numbers)
