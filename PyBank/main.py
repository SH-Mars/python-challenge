# PyBank
import pandas as pd

# read in csv file
df = pd.read_csv("PyBank/Resources/budget_data.csv")
#print(df.head())

# get total number of months by the length of dataset
total_month = len(df)

# get net total amount of "Profit/Losses"
total = df['Profit/Losses'].sum()

# create a list called "diff" for the changes
diff = [0]

# loop through the dataset to calculate the changes by each month
# attach the changes to diff list
for i in range(1, len(df)):
    value1 = df.iloc[i-1][1]
    value2 = df.iloc[i][1]
    change = value2 - value1
    diff.append(change)

# add a new 'change' column with values to the df 
df['change'] = diff

# round up the result of the average of changes
avg_change = round(df['change'][1:].mean(), 2)

# get the maximum in the change column
x = df[df['change'] == df['change'].max()]

# retrieve the month and value from the max above
great_inc_month = x.iloc[0][0]
great_inc_value = x.iloc[0][2]

# get the minimum in the change column
y = df[df['change'] == df['change'].min()]

# retrieve the month and value from the min above
great_dec_month = y.iloc[0][0]
great_dec_value = y.iloc[0][2]

#print out the result according to the instruction
print(f"Financial Analysis")
print("----------------------------")
print(f"Total Month: {total_month}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {great_inc_month} (${great_inc_value})")
print(f"Greatest Decrease in Profits: {great_dec_month} (${great_dec_value})")

# write the result into a text file
output_path = "PyBank/analysis/PyBank_result.txt"
with open(output_path, "w") as file:
    file.write(f"Financial Analysis" + '\n')
    file.write("----------------------------" + '\n')
    file.write(f"Total Month: {total_month}"+ '\n')
    file.write(f"Total: ${total}"+ '\n')
    file.write(f"Average Change: ${avg_change}"+ '\n')
    file.write(f"Greatest Increase in Profits: {great_inc_month} (${great_inc_value})"+ '\n')
    file.write(f"Greatest Decrease in Profits: {great_dec_month} (${great_dec_value})")