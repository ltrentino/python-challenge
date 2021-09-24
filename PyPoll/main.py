# Read CSV election_data.csv from Resources
import os
import csv
csvpath = os.path.join('C:/Users/Laura/Desktop/Homework/python-challenge/PyPoll/Resources/election_data.csv')

# finding Total Votes"
votes = []

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        votes.append(row[0])

# Printing results to terminal    
print("Election Results\n--------------------")
print(f'Total Votes: {len(votes)}')
