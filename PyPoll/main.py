# Import os module
import os

# Import module for reading CSV files
import csv

# Path to CSV file
dirname = os.path.dirname(__file__)
csv_path_election = os.path.join(dirname, 'Resources', 'election_data.csv')

# Read in CSV file
with open(csv_path_election, 'r') as csvfile:
    
    # Specify delimiter
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header
    header = next(csvreader)
    
    # Begin loop through rows
    
    # votesPerCandidate dictionary where key is candidate name, votes are value
        # votesPerCandidate = {name : number of votes}
    votesPerCandidate = {}
    
    # declare each line in csv as variable
    for ballot in csvreader:
        
        # Get the name of the candidate in each line
        currentCandidate = ballot[2]

        # Get number of votes the current candidate has (default to 0) and increase by 1
        candidateVotes = votesPerCandidate.get(currentCandidate, 0)
        votesPerCandidate.update({currentCandidate: candidateVotes + 1})
    
    # Get total sum of all votes
    totalVotes = 0
    for candidateVotes in votesPerCandidate.values():
        totalVotes = totalVotes + candidateVotes

    # Create percentagePerCandidate dictionary
    # Find the winner
    percentagePerCandidate = {}
    winner = ""
    for candidate in votesPerCandidate.keys():
        percentagePerCandidate[candidate] = (votesPerCandidate[candidate] / totalVotes)
        if votesPerCandidate[candidate] > votesPerCandidate.get(winner, 0):
            winner = candidate    

# Print results

# Assign variable to results list
candidateResults = []
for candidate in votesPerCandidate:
    candidateResults.append(f'{str(candidate)}: {"{:.2%}".format(percentagePerCandidate[candidate])} ({str(votesPerCandidate[candidate])})')

# Assign results to list (and insert candidateResults variable into middle of list by using spread operator)
lines = [f"Election Results",
         f"----------------",
         f"Total Votes: {str(totalVotes)}",
         *candidateResults,
         f"----------------",
         f"Winner: {str(winner)}"]

# assign variable to list to print
outputString = '\n'.join(lines)

# Print to terminal
print(outputString)

# Open path to text file
path_results = os.path.join('.', 'Analysis', 'PyPollResults.csv')

# Write in text file
with open(path_results, 'w') as f:
    f.writelines(outputString)