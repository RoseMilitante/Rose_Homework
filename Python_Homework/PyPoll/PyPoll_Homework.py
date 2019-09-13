# dependencies
import os
import csv

# filepath
csvpath = os.path.join("Resources", "election_data.csv")

# declare my variables
names = []
candidates = []
vote_counter = []
percentage_of_votes = []

# Find the total number of votes cast
# Since each row in the csv file is a vote
# I will just count the lines in the file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    total_votes = len(list(csvreader))

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
 
    #take in all the names people voted for and store that into a list
    for x in csvreader:
        names.append(x[2])

#sort the list of names alphabetically        
sorted_names = sorted(names)

#create a new list called candidates of only the unique names
for someone in range(total_votes):
    if sorted_names[someone-1] != sorted_names[someone]:
        candidates.append(sorted_names[someone])

#come up with a total of unique candidte names
total_candidates = len(candidates)        


#using a double for loop, create 2 lists
#one to store the total votes each candidate received
#another to store the percentage of votes each candidate received
for people in range(total_candidates):
    votes = 0
    
    for avote in range(total_votes):
        if sorted_names[avote] == candidates[people]:
            votes += 1 
    vote_counter.append(votes)
    percentage_of_votes.append(round((votes/total_votes * 100),2))    

# print the totals to the terminal
print("-"*25)
print("Election Results")
print("-"*25)
print(f"Total Votes: {total_votes}")
print("-"*25)

combined_stats = zip(candidates, vote_counter, percentage_of_votes)
for each in combined_stats:
    print(f'{each[0]}: {each[2]}% ({each[1]})')

# figure out who won by comparing which number in my
# vote_counter list is the largest
# and then you take that place holder called 'most'
# and find that same spot in the candidates list
# to find the winner's name
for most in range(total_candidates):
    if vote_counter[most] > vote_counter[most - 1]:
        winner = candidates[most]

print("-"*25)
print(f'Winner: {winner}')
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
    file.write(f"Winner: {winner}\n")
    file.write("---------------------------\n")