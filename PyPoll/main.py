# Read CSV election_data.csv from Resources
import os
import csv
csvpath = os.path.join('C:/Users/Laura/Desktop/Homework/python-challenge/PyPoll/Resources/election_data.csv')


# Trying something different to count number of occurrences for each element in Candidate. 
# Found "Counter" in python collections

from collections import Counter
candidate=[]
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        candidate.append(row[2])
#print(Counter(candidate)) # it works!
candidate_dict = dict(Counter(candidate)) # this finds each candidate's votes and puts them in a dict
tot_votes = sum((candidate_dict.values()))
winner = max(candidate_dict, key=candidate_dict. get) # this gets the key of max value


# Printing analysis in terminal
print('Election Results')
print('---------------------------')
print(f'Total Votes: {tot_votes}')
print('---------------------------')
for key in candidate_dict:
    print(f'{key}: {round(candidate_dict[key]/tot_votes*100,3)}% ({candidate_dict[key]})')
print('---------------------------')
print(f'Winner: {winner}')
print('----------------------------')


# Exporting a text file with the results
output_path = os.path.join('C:/Users/Laura/Desktop/Homework/python-challenge/PyPoll/analysis/new.csv')
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow([f'Total Votes: {tot_votes}'])
    csvwriter.writerow(["---------------------"])
    for key in candidate_dict:
        csvwriter.writerow([f'{key}: {round(candidate_dict[key]/tot_votes*100,3)}% ({candidate_dict[key]})'])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow([f'Winner: {winner}'])