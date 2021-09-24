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

with open(csvpath, encoding='utf-8') as csvfile:
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

# Printing results to terminal    
print("Financial Analysis\n--------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(total)}')
print(f'Average Change: ${round(average(change),2)}')
greatest_increase_month = (months[change.index(max(change))+1]) # index + 1 to account for change list having one less element
greatest_decrease_month = (months[change.index(min(change))+1]) # index + 1 to account for change list having one less element
print(f'Greatest Increase in Profits: {greatest_increase_month} (${max(change)})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${min(change)})')

# exporting a text file with the results
output_path = os.path.join('C:/Users/Laura/Desktop/Homework/python-challenge/PyBank/analysis/new.csv')
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow([f'Total Months: {len(months)}'])
    csvwriter.writerow([f'Total: ${sum(total)}'])
    csvwriter.writerow([f'Average Change: ${round(average(change),2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${max(change)})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${min(change)})'])
