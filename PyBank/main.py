# Read CSV budget_data.csv from Resources
import os
import csv
#csvpath = os.path.join('Resources', 'budget_data.csv')
csvpath = os.path.join('C:/Users/Laura/Desktop/Homework/python-challenge/PyBank/Resources/budget_data.csv')

#-----create function for Average-----
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
#-------------------------------------

# finding total number of months and net total of "Profit/Losses"
months = []
total = []
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        months.append(row[0])
        total.append(int(row[1]))
        
# finding change...
for row in total:
    i = total.index(row)
    if i > 0:
        change.append(total[i]-total[i-1])
        

print("Financial Analysis\n--------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(total)}')
print(f'Average Change: ${round(average(change),2)}')
# index + 1 to account for change list having one less element
greatest_increase_month = (months[change.index(max(change))+1])
greatest_decrease_month = (months[change.index(min(change))+1])
print(f'Greatest Increase in Profits: {greatest_increase_month} (${max(change)})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${min(change)})')












