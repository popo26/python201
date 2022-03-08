# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

import pathlib
import csv

path = pathlib.Path(r"C:\Users\Ai\Documents\_CodingNomads\201-lab\03_file-input-output\file-counter-analysis\filecounts.csv")

# with open(path, "a") as file:
#     file.write("\n8,8,8,8")

with open(path, "r") as file:
    print(file.read())

