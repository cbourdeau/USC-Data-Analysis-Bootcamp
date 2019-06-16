# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources" , "budget_data.csv")

# Create lists to store data
month = []
profit_loss_table = []
NewPL = []
OldPL = []
amount_change = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Loop through records
    for row in csvreader:
       month.append(row[0])
       profit_loss_table.append(int(row[1]))
    
    total_amount = sum(profit_loss_table)
    NewPL = profit_loss_table[1:]
    OldPL = profit_loss_table[:-1]

    amount_change = [new - old for (new, old) in zip(NewPL, OldPL)]
    avg_change = (sum(amount_change) / len(amount_change))
    
    #print(max(amount_change))
    month_adjusted = month[1:]
    month_and_change = zip(month_adjusted, amount_change)
    print(month_and_change)

    #greatest_inc_profits = [max(y) for (x,y) in zip(month[1:], amount_change)]
    #print(greatest_inc_profits)

# print final hw
    print("----------------------------")
    print("Finacial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(month)))
    print("Total: " + str(total_amount))
    print("Average Change: " + str(avg_change))