import csv
import os

os.system(f"py.test --csv tests.csv --csv-columns markers")

with open('tests.csv', 'r') as csv_file:
    
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    sample_count = {}
    new_data = []
    
    for line in csv_reader:
        if "," in line[0]:
            new_line = line[0].split(",")
            for l in new_line:
                new_data.append(l)
        else:
            new_data.append(line[0])
            
    for new_line in new_data:   
        # print(new_line)
        if new_line not in sample_count:
            sample_count[new_line] = 1
        else:
            sample_count[new_line] += 1

print(sample_count)
