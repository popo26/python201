# Use the `csv` module to read in and count the different file types.

import csv
import os
import pathlib

path = pathlib.Path().cwd()
print(path)

count = {"": 0, "csv": 0, "md": 0, "png": 0}
folder = 0
csv_ = 0
md = 0
png = 0
for filepath in path.iterdir():
    print(filepath.name)
    if filepath.suffix == "":
        folder += 1
        count.update({"": folder})
    elif filepath.suffix == ".csv":
        csv_ += 1
        count.update({"csv": csv})
    elif filepath.suffix == ".md":
        md += 1
        count.update({"md": md})
print(count)
    
