# Import modules
import os
import csv

# Define Path
pollpath = os.path.join('Resources','election_data.csv')

# Names lists
candidates = []
votedcandidates = []
pervotes = []
candidatevotes = []
List = []

# Define variables for vote counts and percentages
votes = 0
percentage = 0
mostvoted = 0

# Read CSV file
with open(pollpath,'r') as pollfile:

    # Specifie delimeter
    pollreader = csv.reader(pollfile,delimiter=',')

    # Skip header
    pollheader = next(pollreader)

    # Read each row on csv after header
    for row in pollreader:

        # Turn CSV file candidates data into list
        candidates.append(row[2])
    
# Sort Candidates
sortedcandidates = sorted(candidates)

# Loop through large list and find unique candidates and ad them to the new list
for i in range(len(sortedcandidates)):
    if sortedcandidates[i]!= sortedcandidates[i-1]:
        votedcandidates.append(sortedcandidates[i-1])

# Loop through list to calculate votes
for candidate in votedcandidates:

    # Loop throw rows to sum votes for each candidate
    for i in range(len(candidates)):
        # Calculate Votes 
        if candidates[i] == candidate:
            votes = votes+1
    # Add total votes per candidate to list
    candidatevotes.append(votes)
    # Calculate percentages and assign correct format
    percentage = float(float(votes)/float(len(sortedcandidates)))*100
    pervotes.append(f'{percentage:.3f}%')
    # Reset Votes for next candidate
    votes = 0

# Loop through new lists to find who got the most votes
for i in range(len(candidatevotes)):
    if candidatevotes[i] > candidatevotes[i-1]:
        mostvoted = i

# Zip lists for individual candidates results
individualresults = list(zip(votedcandidates,pervotes,candidatevotes))
for somethingelse in individualresults:    
    List.append(somethingelse)

# Make list look pretty
ResultList = ""
for element in List:
    ResultList += f"{element[0]}: {element[1]} ({element[2]}) \n"

# Make Results into a variable for easy text file export
Results = (
    f"Election Results \n"
    f"------------------------------ \n"
    f"Total Votes: {len(sortedcandidates)} \n"
    f"------------------------------ \n"
    f"{ResultList}"
    f"------------------------------ \n"
    f"Winner: {votedcandidates[int(mostvoted)]}")

# Print Results on terminal
print (Results)

#ERROR TESTING ???? 
print (votedcandidates)

#Define output path
Pollout = os.path.join('Analysis',"PyPoll.txt")

# Export results to text file
with open(Pollout, 'w') as txtfile:
    txtfile.writelines(f'{Results}')