# PyPoll

import csv
import os

# csv file path
file_path = os.path.join('Resources', 'election_data.csv')

# follow the instruction to print the result
title = "Election Results"

print(title + "\n" + "-------------------------")

# create empty lists for each of the three columns
vote_ID = []
county = []
candidate = []

# open the file path and read in file, append the values into lists
with open(file_path, "r") as file:
    csvreader = csv.reader(file, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        vote_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# create a dictionary with all the three lists
df = dict({'Voter ID': vote_ID, 
           'County': county, 
           'Candidate': candidate})

# get the total number of votes by the length of the "Voter ID"
total_vote = len(df['Voter ID'])
print(f"Total Votes: {total_vote}"+ "\n" + "-------------------------")

# create three empty lists for further calculation
uni_can = []
can_votes = []
perc = []

# loop through candidate to get the unique candicate names into uni_can list
# at the same time, specify the candidate got 0 vote (to create a element into the can_votes list) 
for i in range(len(df['Candidate'])):
    if df['Candidate'][i] not in uni_can:
        uni_can.append(df['Candidate'][i])
        can_votes.append(0)
    # loop through uni_can list
    for j in range(len(uni_can)):
        # if the the Candidate data is the same as the candidate name in the uni_can list
        if df['Candidate'][i] == uni_can[j]:
            # increase the votes that the candidate received by 1
            can_votes[j] += 1 

# loop through can_votes list to calculate the percentage of votes each candidate won
for k in range(len(can_votes)):
    # calculate the percentage and round to 3 
    percentage = round(can_votes[k]/total_vote*100, 3)
    # append percentage to perc list
    perc.append(percentage)

print(f"{uni_can[0]}: {perc[0]}% ({can_votes[0]})")
print(f"{uni_can[1]}: {perc[1]}% ({can_votes[1]})")
print(f"{uni_can[2]}: {perc[2]}% ({can_votes[2]})"+ "\n" + "-------------------------")

# create a second dictionary with the three lists
df2 = dict({'Candidate': uni_can, 
            'Votes': can_votes,
            'Percentage of Votes': perc})

# loop through Votes
for i in range(1, len(df2['Votes'])):
    # if the votes that previous candidate got is greater
    if df2['Votes'][i-1] > df2['Votes'][i]:
        # assign the candidate name to winner variable
        winner = df2['Candidate'][i-1]
print(f"Winner: {winner}"+ "\n" + "-------------------------")

# write the output to txt file
output_path = "analysis/PyPoll_result.txt"
with open(output_path, "w") as file:
    file.write("Election Results" + '\n')
    file.write("-------------------------" + '\n')
    file.write(f"Total Votes: {total_vote}" + '\n')
    file.write("-------------------------" + '\n')
    file.write(f"{uni_can[0]}: {perc[0]}% ({can_votes[0]})" + '\n')
    file.write(f"{uni_can[1]}: {perc[1]}% ({can_votes[1]})" + '\n')
    file.write(f"{uni_can[2]}: {perc[2]}% ({can_votes[2]})" + '\n')
    file.write("-------------------------" + '\n')
    file.write(f"Winner: {winner}" + '\n')
    file.write("-------------------------")

# #------------------------------------------------------------------------
# # solve the task using pandas dataframe
# import pandas as pd

# # Read in csv file
# df = pd.read_csv('PyPoll\\Resources\\election_data.csv')
# #print(df.head())

# # get the total votes by retrieve number of rows
# total_vote = df.shape[0]
# #print(total_vote)

# # get all the candicate names
# candicate = df['Candidate'].unique()
# #print(candicate)

# # calculate the votes for each candidate
# votes_by_cand = df.groupby('Candidate')['Ballot ID'].count()
# #print(votes_by_cand)

# # calculate the percentage
# perc = votes_by_cand / len(df)
# perc = round(perc * 100, 3)
# #print(perc)

# # combine candidate, votes, and percentage into a dataframe
# ana_df = pd.DataFrame({'Candidate': candicate, 
#                        'Votes': votes_by_cand, 
#                        'Percentage Won': perc})
# ana_df.reset_index(drop=True, inplace=True)
# #print(ana_df)

# # sort descending by Votes to see who's the winner
# ana_df.sort_values(by='Votes', ascending=False, inplace=True)
# winner = ana_df.iloc[0][0]
# #print(winner)

# # print out the result according to the instruction
# print("Election Results")
# print("-------------------------")
# print(f"Total Votes: {total_vote}")
# print("-------------------------")
# print(f"{candicate[0]}: {perc[0]}% ({votes_by_cand[0]})")
# print(f"{candicate[1]}: {perc[1]}% ({votes_by_cand[1]})")
# print(f"{candicate[2]}: {perc[2]}% ({votes_by_cand[2]})")
# print("-------------------------")
# print(f"Winner: {winner}")
# print("-------------------------")

# # write the result into a txt file
# output_path = "PyPoll/analysis/PyPoll_result.txt"
# with open(output_path, "w") as file:
#     file.write("Election Results" + '\n')
#     file.write("-------------------------" + '\n')
#     file.write(f"Total Votes: {total_vote}" + '\n')
#     file.write("-------------------------" + '\n')
#     file.write(f"{candicate[0]}: {perc[0]}% ({votes_by_cand[0]})" + '\n')
#     file.write(f"{candicate[1]}: {perc[1]}% ({votes_by_cand[1]})" + '\n')
#     file.write(f"{candicate[2]}: {perc[2]}% ({votes_by_cand[2]})" + '\n')
#     file.write("-------------------------" + '\n')
#     file.write(f"Winner: {winner}" + '\n')
#     file.write("-------------------------")
#     file.write(f"{candicate[0]}: {perc[0]}% ({votes_by_cand[0]})" + '\n')
#     file.write(f"{candicate[1]}: {perc[1]}% ({votes_by_cand[1]})" + '\n')
#     file.write(f"{candicate[2]}: {perc[2]}% ({votes_by_cand[2]})" + '\n')
#     file.write("-------------------------" + '\n')
#     file.write(f"Winner: {winner}" + '\n')
#     file.write("-------------------------")