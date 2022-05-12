import csv
import os
from collections import defaultdict

os.system(f"py.test --csv tests.csv --csv-columns markers,function")

# open generated csv
with open('tests.csv', 'r') as csv_file:
    
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    counts = defaultdict(dict)
    
    methods = defaultdict(list)
    new_methods = defaultdict(dict)
    
    result = {}
    for line in csv_reader:
        # split the list to loop them 1 by 1
        if "," in line[0]:
            new_line = line[0].split(",")
            
            for l in new_line:
                # append the method names to methods
                methods[l].append(line[1])
                
                # put counts to counts dictionary
                if l not in counts:
                    counts[l]['count'] = 1
                else:
                    counts[l]['count'] += 1
        else: 
            if line[0] not in counts:
                counts[line[0]]['count'] = 1
            else:
                counts[line[0]]['count'] += 1
      
    # naming the values as methods      
    for k, v in methods.items():
        new_methods[k]['methods'] = v
        
    new_methods = dict(new_methods)
    counts = dict(counts)
    
    # combining the 2 dictionary by keys
    for key in (new_methods.keys() | counts.keys()):
        if key in new_methods: result.setdefault(key, []).append(new_methods[key])
        if key in counts: result.setdefault(key, []).append(counts[key])
    
print(result)

# collect pytest