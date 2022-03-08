# Write the file counts to a `.csv` file.

import csv

with open("filecounts.csv", "w") as csvfile:
    print(csvfile.write("8,8,8,8"))