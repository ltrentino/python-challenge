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

# to check unique candidates
#print(set(candidate)) # returns O'Tooley, 'Khan', 'Li', 'Correy' --> added these to lists created

# create variables for readability
total_votes = (len(candidate))
khan_votes = (len(khan))
correy_votes = (len(correy))
li_votes = (len(li))
otooley_votes = (len(otooley))

khan_ratio = round((khan_votes / total_votes * 100),3)
correy_ratio = round((correy_votes / total_votes * 100),3)
li_ratio = round((li_votes / total_votes * 100),3)
otooley_ratio = round((otooley_votes / total_votes * 100),3)

print(f'Khan: {khan_ratio}% ({khan_votes})')
print(f'Correy: {correy_ratio}% ({correy_votes})')
print(f'Li: {Li_ratio}% ({Li_votes})')
print(f'O\'Tooley: {otooley_ratio}% ({otooley_votes})')
print("----------------------------------")



# # checking lists len is same
# print(len(votes))   #3521001
# print(len(county))
# print(len(candidate))


