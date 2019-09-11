# dependencies
import os
import csv

# filepath
csvpath = os.path.join("Resources", "budget_data.csv")

# declare my variables
net_profit_losses = []
p_l_changes = []
dates = []


#open up the file and skip the header row
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)
    
    #retrieve all the profit/loss values and store in a list called net_profit_losses
    #retrieve all the date values and store in a list called dates 
    for row in csvreader:
        net_profit_losses.append(int(row[1]))
        dates.append(row[0])
    
    #calculate the difference in profit and loss changes
    #by taking each next value and subtracting that from the previous value
    for number in range(1, len(net_profit_losses)):
        p_l_changes.append((int(net_profit_losses[number]))- int(net_profit_losses[number-1]))

#calculate the number of months for which we received data for
#by counting how many rows of data we received, not including the header
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    total_months = len(list(csvreader))

# Calculate the net total amount of "Profit/Losses" over the entire period.
Sum = sum(net_profit_losses)


# The average of the changes in "Profit/Losses" over the entire period
length = len(p_l_changes)
sum_of_changes = sum(p_l_changes)
Average = sum_of_changes / length

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(p_l_changes)
position_of_greatest_increase = p_l_changes.index(greatest_increase)
greatest_increase_date = dates[position_of_greatest_increase + 1]

# The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(p_l_changes)

# find the index of the greatest decrease
# to find the corresponding date of the greatest decrease
# since we are comparing 2 dates for each change, we want the later date
# which is why we need to add 1 to the index
position_of_greatest_decrease = p_l_changes.index(greatest_decrease)
greatest_decrease_date = dates[position_of_greatest_decrease + 1]

# Print my analysis to the terminal
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(Sum)}")
print(f"Average Change: ${str(round(Average, 2))}")
print(f"Greatest Increase in Profits: {greatest_increase_date}  $({str(round(greatest_increase, 2))})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date}  $({str(round(greatest_decrease, 2))})")
print("---------------------------")

# Add this Financial Analysis info to a text file
# Specifiy the file to write to
output_path = os.path.join("output","pybanks_output.txt")

# Open the file using "write" mode and write the info to the file
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------\n")
    file.write(f"Total Months: {str(total_months)}\n")
    file.write(f"Total: ${str(Sum)}\n")
    file.write(f"Average Change: ${str(round(Average, 2))}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date}  $({str(round(greatest_increase, 2))})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date}  $({str(round(greatest_decrease, 2))})\n")
    file.write("---------------------------\n")