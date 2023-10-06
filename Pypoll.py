import os
import csv

# Create the lists to store data.

count = 0
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []

# Set the path for the csv file
# <path>/<to>/Week3Assignment/Resources/election_data.csv
election_data_csv = os.path.join("Resources", "election_data.csv")

# with open as csvfile
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)
    
    # Initiate the count
    for row in csvreader:
        
        # Track the count of total number of votes
        count = count + 1
        
        # Track the candidate names via candidate_List
        candidate_list.append(row[2])
        
        # Create 1st set from the candidate_list using "x" to retrieve candidate names
    for x in set(candidate_list):
        unique_candidate.append(x)
        
        # Create 2nd set for total votes for each candidate using "y"
        y = candidate_list.count(x)
        vote_count.append(y)
        
        # Create 3rd set for the % of total vote for each candidate using "z" 
        z = (y/count)*100
        vote_percent.append(z)
    
    # Track the winning vote count using max
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

# Print out the candidate election results.

print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(round(vote_percent[i],3)) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Print results to a .txt file

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")