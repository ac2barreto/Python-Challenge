# Import modules
import os
import csv

# Define Path
bankpath = os.path.join('Resources',"budget_data.csv")

# Names lists
month = []
profit = []
profitvar = []


# Read CSV file as module
with open(bankpath, 'r') as bankfile:

    # Specifie delimeters of data
    bankreader = csv.reader(bankfile, delimiter=',')
    
    # Skip csv header
    bankheader = next(bankfile)

    # Read each row on csv after header
    for row in bankreader:
       
        # Turn csv columns into lists casting values to correct format
        month.append(row[0])
        profit.append(int(row[1]))

    # Define my variable "profitvar" used later to calculate changes in profit
    for i in range(int(len(profit))-1): 
        profitvar.append(int(profit[i+1])-int(profit[i]))

# Find variation extremes
gincrease = int(max(profitvar))
gdecrease = int(min(profitvar))

# Loop through list and find the position for greatest variations
for i in range(len(profitvar)):
    if profitvar[i] == gincrease:   
        giposition = (i+1) 

for i in range(len(profitvar)):
    if profitvar[i] == gdecrease:
        gdposition = (i+1)

# Make analysis into a variable to not repeat when exporting to text file
Analysis = (
    f"Financial Analysis \n"
    f"------------------------------ \n"
    f"Total Months:{len(month)} \n"
    f"Total: ${int(sum(profit))} \n"
    f"Average Change: ${float(int(sum(profitvar))/int(len(profitvar))):.2f} \n"
    f"Greatest Increase in profits: {month[giposition]} (${gincrease}) \n"
    f"Greatest Decrease in Profits: {month[gdposition]} (${gdecrease}) \n")

#Print Analysis on terminal
print(Analysis)

#Define output path
bankout = os.path.join('Analysis',"PyBank.txt")

# Export results to text file
with open(bankout, 'w') as txtfile:
    txtfile.writelines(f'{Analysis}')