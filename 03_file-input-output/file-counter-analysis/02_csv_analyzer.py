# Use the `csv` module to read in and count the different file types.


import csv

count = {'folder': 2, 'deb': 3, 'md': 0, 'zip': 3} ##code to count different file types are in 01_csv_writer.py

with open("03_file-input-output/file-counter-analysis/filecounts.csv","a") as file:
    # print(file.read())

    #write header###
    fieldnames = ['folder', 'deb', 'md', 'zip']
    countwriter=csv.DictWriter(file, fieldnames=fieldnames)
    # countwriter.writeheader() ##Unless you want to see new headers everytime, comment it out.

    #Adding dictionary values to file###
    countwriter = csv.writer(file)
    data = [count["folder"], count["deb"], count["md"], count["zip"]]
    countwriter.writerow(data)





    ##so many erros

    # use dictionary with file type/count