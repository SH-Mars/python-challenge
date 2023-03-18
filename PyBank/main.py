# PyBank

import csv

# specify the file path
file_path = "C:\\Users\\s4013\\OneDrive\\Documents\\UCB Data Bootcamp\\Python\\Week 3\\Challenge 3\\python-challenge\\PyBank\\Resources\\budget_data.csv"

# following the format according to instruction
title = "Financial Analysis"
print(title + "\n" + "----------------------------")

# create two empty list to store two columns of data in csv
date = []
profit_loss = []

# open the csv file in read mode and read the data into list by appending
with open(file_path, "r") as file:
    csvreader = csv.reader(file, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])

# zip the two lists into a zip object
df = list(zip(date, profit_loss))

# get the total number of months by the length of the data
total_month = len(df)
print(f"Total Months: {total_month}")

# specify the total variable for the net total amount of "Profit/Losses"
total = 0

# loop through the df to calcualte the net total
for i in range(len(df)):
   value = df[i][1]
   total += int(value)
print(f"Total: ${total}")

# create an empty list for changes in "Profit/Losses"
change = [0]

# loop through df to calculate the changes and append the value back to change list
for i in range(1, len(df)):
    value1 = int(df[i-1][1])
    value2 = int(df[i][1])
    diff = value2 - value1
    change.append(diff)

# make the change list into int type
change = list(map(int, change))

# have date, profit_loss, and change into a dictionary
df = dict({'date': date, 
           'profit_loss': profit_loss,
           'change': change})

# create a variable, sum_diff, for the sum of changes
sum_diff = 0
for i in range(1, len(df['change'])):
    sum_diff += df['change'][i]
# calculate the average of changes and round to 2 decimal places
avg_change = round(sum_diff / (len(df['change'])-1), 2)
print(f"Average Change: ${avg_change}")

# create two variables for the max change value and the greatest increase period
# specify the value as the first row we have in the csv
max = df['change'][0]
greatest_month = df['date'][0]
# loop through the data
for i in range(1, len(df['date'])):
    # if the df['change'][i] is greater than the current max value
    if df['change'][i] > max:
        # then make max = df['change'][i], and greatest_month = df['date'][i]
        max = df['change'][i]
        greatest_month = df['date'][i]

print(f"Greatest Increase in Profits: {greatest_month} (${max})")

# same concept as how to get the max and greatest_month
min = df['change'][0]
lowest_month = df['date'][0]
for i in range(1, len(df['date'])):
    # if the df['change'][i] is less than current min value
    if df['change'][i] < min:
        # then make min = df['change'][i] and lowest_month = df['date'][i]
        min = df['change'][i]
        lowest_month = df['date'][i]

print(f"Greatest Decrease in Profits: {lowest_month} (${min})")

output_path = "analysis/PyBank_result.txt"
with open(output_path, "w") as file:
   file.write(f"Financial Analysis" + '\n')
   file.write("----------------------------" + '\n')
   file.write(f"Total Month: {total_month}"+ '\n')
   file.write(f"Total: ${total}"+ '\n')
   file.write(f"Average Change: ${avg_change}"+ '\n')
   file.write(f"Greatest Increase in Profits: {max} (${greatest_month})"+ '\n')
   file.write(f"Greatest Decrease in Profits: {min} (${lowest_month})")

#--------------------------------------------------------------------------
# solve the tasks by tuple instead of create a dictionary

# df = list(zip(date, profit_loss, change))

# total_change = 0
# for i in range(1, len(change)):
#     total_change += change[i]
#     avg_change = round(total_change/(len(change)-1), 2)
# print(avg_change)

# maximum = df[0][2]
# greatest_month = df[0][0]
# for i in range(1, len(df)):
#     if df[i][2] > maximum:
#         maximum = df[i][2]
#         greatest_month = df[i][0]

# print(greatest_month)
# print(maximum)

# minimum = df[0][2]
# lowest_month = df[0][0]

# for i in range(1, len(df)):
#     if df[i][2] < minimum:
#         minimum = df[i][2]
#         lowest_month = df[i][0]
# print(lowest_month)
# print(minimum)


#------------------------------------------------------------------------
# slove the tasks using pandas dataframe
# import pandas as pd

# # read in csv file
# df = pd.read_csv("PyBank/Resources/budget_data.csv")
# #print(df.head())

# # get total number of months by the length of dataset
# total_month = len(df)

# # get net total amount of "Profit/Losses"
# total = df['Profit/Losses'].sum()

# # create a list called "diff" for the changes
# diff = [0]

# # loop through the dataset to calculate the changes by each month
# # attach the changes to diff list
# for i in range(1, len(df)):
#     value1 = df.iloc[i-1][1]
#     value2 = df.iloc[i][1]
#     change = value2 - value1
#     diff.append(change)

# # add a new 'change' column with values to the df 
# df['change'] = diff

# # round up the result of the average of changes
# avg_change = round(df['change'][1:].mean(), 2)

# # get the maximum in the change column
# x = df[df['change'] == df['change'].max()]

# # retrieve the month and value from the max above
# great_inc_month = x.iloc[0][0]
# great_inc_value = x.iloc[0][2]

# # get the minimum in the change column
# y = df[df['change'] == df['change'].min()]

# # retrieve the month and value from the min above
# great_dec_month = y.iloc[0][0]
# great_dec_value = y.iloc[0][2]

# #print out the result according to the instruction
# print(f"Financial Analysis")
# print("----------------------------")
# print(f"Total Month: {total_month}")
# print(f"Total: ${total}")
# print(f"Average Change: ${avg_change}")
# print(f"Greatest Increase in Profits: {great_inc_month} (${great_inc_value})")
# print(f"Greatest Decrease in Profits: {great_dec_month} (${great_dec_value})")

# # write the result into a text file
# output_path = "PyBank/analysis/PyBank_result.txt"
# with open(output_path, "w") as file:
#     file.write(f"Financial Analysis" + '\n')
#     file.write("----------------------------" + '\n')
#     file.write(f"Total Month: {total_month}"+ '\n')
#     file.write(f"Total: ${total}"+ '\n')
#     file.write(f"Average Change: ${avg_change}"+ '\n')
#     file.write(f"Greatest Increase in Profits: {great_inc_month} (${great_inc_value})"+ '\n')
#     file.write(f"Greatest Decrease in Profits: {great_dec_month} (${great_dec_value})")