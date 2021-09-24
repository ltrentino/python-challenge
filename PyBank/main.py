# Read CSV budget_data.csv from Resources
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
#csvpath = os.path.join('C:/Users/Laura/Desktop/Homework/python-challenge/PyBank/Resources/budget_data.csv')

months = []
total = []
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        months.append(row[0])
        total.append(int(row[1]))
        
# print(f'Total Months: {len(months)}')
# print(f'Total: ${sum(total)}')

# finding change...
for row in total:
    i = total.index(row)
    if i > 0:
        change.append(total[i]-total[i-1])
print(change)












