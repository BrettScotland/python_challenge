#Imports
import os
import csv

csvpath = os.path.join("Resources", "Budget_data.csv")

rev = []
date = []
rev_change = []




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    next(csvreader, None)

    net_profit_losses = 0

    for row in csvreader:
        rev.append(row[1])
        date.append(row[0])

        net_profit_losses += int(row[1])

for i in range(1, len(rev)):
    rev_change.append(int(rev[i]) - int(rev[i - 1]))
    average_change = sum(rev_change)/len(rev_change)

    max_change = max(rev_change)

    min_change = min(rev_change)

index_max = rev_change.index(max_change)
index_min = rev_change.index(min_change)

date_max = date[index_max + 1]
date_min = date[index_min + 1]

print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${net_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_max} (${max_change})")
print(f"Greatest Decrease in Profits: {date_min} (${min_change})")