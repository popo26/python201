# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():
  # define the function here
  sum_value = sum(example_list)
  max_value = max(example_list)
  min_value = min(example_list)
  ave_value = sum_value / len(example_list)
  return f"Total is {sum_value}\nMaximum number is {max_value}\nMinimum number is {min_value}\nAverange value is {ave_value}"
    

# call the function below here

answer = stats()
print(answer)
