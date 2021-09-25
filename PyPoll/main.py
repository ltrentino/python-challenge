# Read CSV election_data.csv from Resources
import os
import csv
csvpath = os.path.join('C:/Users/Laura/Desktop/Homework/python-challenge/PyPoll/Resources/election_data.csv')

# creating lists
candidate = []
khan = []
correy = []
li = []
otooley = []


with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        # votes.append(row[0])
        # county.append(row[1])
        candidate.append(row[2])
        
        if row[2] == "Khan":
            khan.append(row)
        elif row[2] == "Correy":
            correy.append(row)
        elif row[2] == "Li":
            li.append(row)
        elif row[2] == "O'Tooley":
            otooley.append(row)

print(len(khan))
print(len(correy))
print(len(li))
print(len(otooley))

# to check unique candidates
print(set(candidate)) # returns O'Tooley, 'Khan', 'Li', 'Correy' --> added these to lists created


# # checking lists len is same
# print(len(votes))   #3521001
# print(len(county))
# print(len(candidate))

# # Printing results to terminal    
# print("Election Results\n--------------------")
# print(f'Total Votes: {len(votes)}')





