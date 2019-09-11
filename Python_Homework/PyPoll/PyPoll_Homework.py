# dependencies
import os
import csv

#filepath
csvpath = os.path.join("Resources", "election_data.csv")

#declare my variables
names = {}
votes_received = 0
winner = []
votes = 0

# Find the total number of votes cast
# Since each row in the csv file is a vote
#I will just count the lines in the file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    total_votes = len(list(csvreader))

#print total votes to the terminal
print("-"*25)
print("Election Results")
print("-"*25)
print(f"Total Votes: {total_votes}")
print("-"*25)

# A complete list of candidates who received votes
# here we open up the csv file and read it, skipping the header
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    #look through every row in the csv file and
    #Use candidate_name with each candidate's name 
    #use these names as the key. 
    #look through each row and if that name comes up, add 1 to their each names's counts
    for row in csvreader:
        candidate_name = row[2]
        
        if candidate_name in names.keys():
             names[candidate_name] += 1
        else:
             names[candidate_name] = 1
    
    for candidate_name in names:
        #The percentage of votes each candidate won
        percentage = round((names[candidate_name])/total_votes * 100)
        #The total number of votes each candidate won
        votes_received = names[candidate_name]
        print(f'{candidate_name}: {percentage}% ({votes_received})')

# The winner of the election based on popular vo
winner = list(names.keys())

print("-"*25)
print(f'Winner: {winner[0]}')
print("-"*25)


# Export analysis to a text file with the results
# Specifiy the file to write to
output_path = os.path.join("output","pypoll_output.txt")

# Open the file using "write" mode and write the info to the file
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("---------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("---------------------------\n")
    file.write(f"Winner: {winner[0]}\n")
    file.write("---------------------------\n")
