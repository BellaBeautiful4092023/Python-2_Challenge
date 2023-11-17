import os
import csv

# Correct the path to the CSV file
csvpath = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

# Initialize lists to store voters and votes per candidate
voters_candidates = []
votes_per_candidate = {}
total_votes = 0
winning_count = 0

# Open the CSV file using the correct variable name
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print(header)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Add to total vote count
        total_votes += 1

        # Append candidate names to the list
        voters_candidates.append(row[2])

        # Count votes per candidate
        if row[2] in votes_per_candidate:
            votes_per_candidate[row[2]] += 1
        else:
            votes_per_candidate[row[2]] = 1

# Print the sorted list of candidate names
sorted_candidates = sorted(set(voters_candidates))
#print("Sorted Candidate List:", sorted_candidates)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open(file_to_output, "w") as txt_file:
    output = (f"\nElection Results\n"
            f"------------------\n"
            f"Total Votes: {total_votes}\n"
            f"------------------\n")

    print(output, end = "")
    txt_file.write(output)

    # Print the votes per candidate
    for candidate in votes_per_candidate:
        vote_percentage = (votes_per_candidate[candidate] / total_votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes_per_candidate[candidate]})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes_per_candidate[candidate]})\n")

        if (votes_per_candidate[candidate] > winning_count):
            winning_count = votes_per_candidate[candidate]
            winning_candidate = candidate

    output = (f"------------------\n"
            f"Winner: {winning_candidate}\n\n")

    print(output, end = "")
    txt_file.write(output)

