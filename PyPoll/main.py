import csv

with open('election_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)

import os
import csv

# Path to the CSV file
csvpath = os.path.join("election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Loop through rows
    for row in csvreader:
        # Increment total vote count
        total_votes += 1

        # Add candidate to dictionary or increment vote count
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through candidates and calculate percentages
for candidate, votes in candidate_votes.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
    
    # Determine winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = round((votes / total_votes) * 100, 3)
        txtfile.write(f"{candidate}: {percentage}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

