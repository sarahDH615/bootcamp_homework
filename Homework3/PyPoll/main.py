import os
import csv

#lists to hold values from col1(row[0]) and col2(row[1])
votes = []
candidates = []

#functions to call for finding values from the lists


csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        if row[2] == "Candidate":
            continue
        votes.append(row[2])
        if row[2][0] != row[2]:
            candidates.append(row[2])
               
total_votes = int(len(votes))
print(f"Total Votes: {total_votes}")

unique_names = set(candidates)
print(unique_names)


#print(candidates)