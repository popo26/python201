# Use the `csv` module to read in and count the different file types.

import csv
import os

# with open(r"C:\Users\Ai\Documents\_CodingNomads\201-lab\03_file-input-output\file-counter\filecounts.csv", mode="r") as file:
#     print(file.read())

# with open(r"C:\Users\Ai\Documents\_CodingNomads\201-lab\03_file-input-output\file-counter\filecounts.json", mode="r") as file:
#     print(file.read())

# with open(r"C:\Users\Ai\Documents\_CodingNomads\201-lab\03_file-input-output\file-counter\filecounts.txt", mode="r") as file:
#     print(file.read())

print("hello", os.getcwd())
# file name only doesnt work.
with open(r"\03_file-input-output\file-couter\filecounts.txt", mode="r") as file:
    print(file.read())