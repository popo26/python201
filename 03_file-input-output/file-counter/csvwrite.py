# Write the file counts to a `.csv` file.

import csv

with open("03_file-input-output/file-counter/filecounts.csv", "a") as csvfile:
    # print(csvfile.read())
    print(csvfile.write("\n1,1,1,2"))