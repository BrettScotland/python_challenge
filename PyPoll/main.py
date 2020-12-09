#Imports
import os
import csv

csvpath = os.path.join("Resources", "Election_data.csv")

unique_candidates = []
candidates = []
Khan_counter = 0
OTooley_counter = 0
Li_counter = 0
Correy_counter = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    next(csvreader, None)
    
    for row in csvreader:
        candidates.append(row[2])

        if row[2] == "Khan":
            Khan_counter = Khan_counter + 1
        elif row[2] == "Li":
            Li_counter = Li_counter + 1
        elif row[2] == "Correy":
            Correy_counter = Correy_counter + 1
        else:
            OTooley_counter = OTooley_counter + 1

unique_candidates = set(candidates)

total_votes = len(candidates)

percentage_Khan = round(Khan_counter/total_votes*100, 2)
percentage_OTooley = round(OTooley_counter/total_votes*100, 2)
percentage_Li = round(Li_counter/total_votes*100, 2)
percentage_Correy = round(Correy_counter/total_votes*100, 2)


Results = (f"Election Results\n----------------\nTotal Votes: {total_votes}\n----------------\nKhan: {percentage_Khan}% ({Khan_counter})\nCorrey: {percentage_Correy}% ({Correy_counter})\nLi: {percentage_Li}% ({Li_counter})\nO'Tooley: {percentage_OTooley}% ({OTooley_counter})\n----------------\nWinner: Khan\n----------------")
print(Results)

text_path = os.path.join("Analysis", "Results.txt")
file = open(text_path, "w")
file.write(Results)
file.close()