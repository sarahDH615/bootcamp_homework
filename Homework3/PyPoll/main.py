import os
import csv

#lists to hold values from col1(row[0]) and col2(row[1])
votes = []

#functions to call for finding values from the lists


csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        if row[2] == "Candidate":
            continue
        votes.append(row[2])
    
    election_dictionary = {}
    total = (int(len(votes)))
    total_less_one = total - 1
    election_dictionary["Election Results"] = "_"
    election_dictionary["Total Votes"] = total
    election_dictionary["Candidate"] = "percentage of vote", "number of votes"


    print(f"                         ")
    print("Election Results")
    print(f"_________________________")
    print(f"                         ")
    print(f"Total Votes: {total}")
    print(f"_________________________")

    votes_sorted = sorted(votes)
    #last value is the last name on the list
    last_value = votes_sorted[total_less_one]
    #print(last_value)

    counter = 0
    cand_list = []

    for n in range(0, total_less_one):
        if votes_sorted[n] != votes_sorted[n+1]:
            counter = counter + 1
            percentage_votes = round(((counter/total) *100), 2)
            candidate_data = (votes_sorted[n], percentage_votes, counter)
            cand_list.append(candidate_data)
            election_dictionary [candidate_data[0]] = candidate_data[1], candidate_data[2]
            print(f"{votes_sorted[n]}: {percentage_votes}% ({counter})")
            counter = 0
        elif votes_sorted[n] == votes_sorted[n+1]:
            counter = counter + 1  
        elif rfind(votes_sorted[n+1]) == total_less_one:
            counter = counter + 1
            percentage_votes = round(((counter/total) *100), 2)
            candidate_data = (votes_sorted[n], percentage_votes, counter)
            cand_list.append(candidate_data)
            election_dictionary [candidate_data[0]] = candidate_data[1], candidate_data[2]
            print(f"{votes_sorted[n]}: {percentage_votes}% ({counter})")
            counter = 1
    
    percentage_votes = round(((counter/total) *100), 2)
    candidate_data = (votes_sorted[n], percentage_votes, counter)
    cand_list.append(candidate_data)
    election_dictionary [candidate_data[0]] = candidate_data[1], candidate_data[2]
    print(f"{votes_sorted[n]}: {percentage_votes}% ({counter})")

    cand_list.sort(key = lambda x:x[2])
    election_dictionary ["Winner"] = cand_list[-1][0]

    print(f"_________________________")
    print(f"                         ")
    print(f"Winner: {cand_list[-1][0]}")
    print(f"_________________________")



output_path = os.path.join("Analysis", "pypoll_results.csv")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    for key, value in election_dictionary.items():
        csvwriter.writerow([key, value])

    
    