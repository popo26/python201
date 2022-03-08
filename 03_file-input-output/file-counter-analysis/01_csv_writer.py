# Add your file counter code here.
# Then add more code that writes the file counts to a `.csv` file.

import pathlib
import csv

path = pathlib.Path().cwd()
print(path)

with open(r"C:\Users\Ai\Documents\_CodingNomads\201-lab\03_file-input-output\file-counter-analysis\filecounts.csv", "a") as csvfile:
    csvfile.write("\n13,113,1,1\n13,13,12,12")