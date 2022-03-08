# Add your file counter code here.
# Then add more code that writes the file counts to a `.csv` file.

import csv
import pathlib

path = pathlib.Path("/home/popo26/Downloads")
print(path)

count = {"folder": 0, "deb": 0, "md": 0, "zip": 0}
folder = 0
deb = 0
md = 0
zip = 0
for filepath in path.iterdir():
    print(filepath.name)
    if filepath.suffix == "":
        folder += 1
        count.update({"folder": folder})
    elif filepath.suffix == ".deb":
        deb += 1
        count.update({"deb": deb})
    elif filepath.suffix == ".md":
        md += 1
        count.update({"md": md})
    elif filepath.suffix == ".zip":
        zip += 1
        count.update({"zip": zip})
print(count)

with open("03_file-input-output/file-counter-analysis/filecounts.csv", "a") as csvfile:
    csvfile.write(str(count))
    csvfile.write("\n")