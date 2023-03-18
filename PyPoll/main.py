# PyPoll
import pandas as pd

# Read in csv file
df = pd.read_csv('PyPoll\\Resources\\election_data.csv')
#print(df.head())

# get the total votes by retrieve number of rows
total_vote = df.shape[0]
#print(total_vote)

# get all the candicate names
candicate = df['Candidate'].unique()
#print(candicate)

# calculate the votes for each candidate
votes_by_cand = df.groupby('Candidate')['Ballot ID'].count()
#print(votes_by_cand)

# calculate the percentage
perc = votes_by_cand / len(df)
perc = round(perc * 100, 3)
#print(perc)

# combine candidate, votes, and percentage into a dataframe
ana_df = pd.DataFrame({'Candidate': candicate, 
                       'Votes': votes_by_cand, 
                       'Percentage Won': perc})
ana_df.reset_index(drop=True, inplace=True)
#print(ana_df)

# sort descending by Votes to see who's the winner
ana_df.sort_values(by='Votes', ascending=False, inplace=True)
winner = ana_df.iloc[0][0]
#print(winner)

# print out the result according to the instruction
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_vote}")
print("-------------------------")
print(f"{candicate[0]}: {perc[0]}% ({votes_by_cand[0]})")
print(f"{candicate[1]}: {perc[1]}% ({votes_by_cand[1]})")
print(f"{candicate[2]}: {perc[2]}% ({votes_by_cand[2]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# write the result into a txt file
output_path = "PyPoll/analysis/PyPoll_result.txt"
with open(output_path, "w") as file:
    file.write("Election Results" + '\n')
    file.write("-------------------------" + '\n')
    file.write(f"Total Votes: {total_vote}" + '\n')
    file.write("-------------------------" + '\n')
    file.write(f"{candicate[0]}: {perc[0]}% ({votes_by_cand[0]})" + '\n')
    file.write(f"{candicate[1]}: {perc[1]}% ({votes_by_cand[1]})" + '\n')
    file.write(f"{candicate[2]}: {perc[2]}% ({votes_by_cand[2]})" + '\n')
    file.write("-------------------------" + '\n')
    file.write(f"Winner: {winner}" + '\n')
    file.write("-------------------------")