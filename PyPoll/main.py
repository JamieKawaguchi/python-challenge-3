import os
import csv

election_data= os.path.join ("Documents", "Bootcamp", "python-challenge", "PyPoll", "Resources", "election_data.csv")

with open (election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)

    total_votes = 0
    candidate_votes = {}

    for row in csv_reader:
        total_votes += 1
        candidate = row[2] 

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    print(f"Total Votes: {total_votes}")
    print("Candidates who received votes:")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.2f}% ({votes} votes)")

    winner = max(candidate_votes, key=candidate_votes.get)
    print(f"Winner: {winner} with {candidate_votes[winner]} votes")

    with open(output_file, 'w') as output:
                output.write(f"Total Votes: {total_votes}\n")
                output.write("Candidates who received votes:\n")
                for candidate, votes in candidate_votes.items():
                    percentage = (votes / total_votes) * 100
                    output.write(f"{candidate}: {percentage:.2f}% ({votes} votes)\n")
                output.write(f"Winner: {winner} with {candidate_votes[winner]} votes\n")
