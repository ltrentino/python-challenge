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
print(Counter(candidate))



# # creating candidate variable
# candidate = []
# # each candidate found with set function (see line 33) needs variable
# khan = []
# correy = []
# li = []
# otooley = []

# with open(csvpath, encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ',')
#     csv_header = next(csvreader)
#     for row in csvreader: 
#         candidate.append(row[2])
#         # populating individual candidates lists
#         if row[2] == "Khan":
#             khan.append(row)
#         elif row[2] == "Correy":
#             correy.append(row)
#         elif row[2] == "Li":
#             li.append(row)
#         elif row[2] == "O'Tooley":
#             otooley.append(row)

# # to check unique candidates
# set(candidate) # returns O'Tooley, 'Khan', 'Li', 'Correy' --> added these to lists created


# # create Candidates list for print output
# candidate_list = ["Khan","Correy","Li","O'tooley"]

# # create Votes variables for readability
# khan_votes = (len(khan))
# correy_votes = (len(correy))
# li_votes = (len(li))
# otooley_votes = (len(otooley))
# total_votes = (len(candidate))
# # create list of Votes for print output
# votes_list = [khan_votes, correy_votes, li_votes, otooley_votes]

# # create Ratios variables for readibility
# khan_ratio = round((khan_votes / total_votes * 100),3)  #not sure how to add three decimals, round3 is not working
# correy_ratio = round((correy_votes / total_votes * 100),3)
# li_ratio = round((li_votes / total_votes * 100),3)
# otooley_ratio = round((otooley_votes / total_votes * 100),3)
# # create list of Ratios for print output
# ratio_list = [khan_ratio, correy_ratio, li_ratio, otooley_ratio]

# # find Winner and store variable
# maxvalue = max(ratio_list)
# winner_index = ratio_list.index(maxvalue)
# winner = candidate_list[winner_index]


# print("Election Results")
# print("-------------------")
# print(f'Total Votes: {total_votes}')
# for x,y,z in zip(candidate_list, ratio_list, votes_list):
#     print(f' {x} : {y}% ({z})')
# print("-------------------")
# print(f'Winner: {winner}')
# print("-------------------")

# # exporting a text file with the results
# output_path = os.path.join('C:/Users/Laura/Desktop/Homework/python-challenge/PyPoll/analysis/new.csv')
# with open(output_path, 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',')
#     csvwriter.writerow(["Election Results"])
#     csvwriter.writerow(["---------------------"])
#     csvwriter.writerow([f'Total Votes: {total_votes}'])
#     csvwriter.writerow(["---------------------"])
#     csvwriter.writerow([f'{candidate_list[0]}: {ratio_list[0]}% ({votes_list[0]})'])
#     csvwriter.writerow([f'{candidate_list[1]}: {ratio_list[1]}% ({votes_list[1]})'])
#     csvwriter.writerow([f'{candidate_list[2]}: {ratio_list[2]}% ({votes_list[2]})'])
#     csvwriter.writerow([f'{candidate_list[3]}: {ratio_list[3]}% ({votes_list[3]})'])
#     csvwriter.writerow(["---------------------"])
#     csvwriter.writerow([f'Winner: {winner}'])
