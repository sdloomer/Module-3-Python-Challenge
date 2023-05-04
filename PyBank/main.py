# Import os module
import os

# Import module for reading CSV files
import csv

# Specify CSV file
budget_path = os.path.join('.', 'Resources', 'budget_data.csv')

# Open CSV file using csvreader
with open(budget_path, 'r') as budget_file:

    # Specify delimiter
    csvreader = csv.reader(budget_file, delimiter=',')

    # Skip header
    header = next(csvreader)

    # Begin loop through lows

    # Set variables equal to zero or empty (to fill with value during loop)
    totalmonths = 0
    totalprofits = 0
    firstMonth = 0
    currentmonthprofits = 0
    previousmonthprofits = 0
    totalchange = 0
    averagechange = 0
    maxProfitDelta = 0
    minProfitDelta = 0
    maxDeltaMonth = ""
    minDeltaMonth = ""
    
    # Declare each line in csv as variable 'rowData'
        # Add one for each line, add all row index[1] together

    for rowIndex, rowData in enumerate(csvreader):
        totalmonths = totalmonths + 1
        currentmonthprofits = int(rowData[1])
        totalprofits = totalprofits + currentmonthprofits
        
        # To prevent average and total changes of zero for the second line (rowIndex[1]) assign currentmonthprofits 
            #to previousmonthprofits
        if (rowIndex == 0):
            previousmonthprofits = currentmonthprofits

        # Reinitialize min and max profit delta and months to be the first profit delta
        profitDelta = int(currentmonthprofits) - int(previousmonthprofits)
        if (rowIndex == 1):
            minProfitDelta = profitDelta
            maxProfitDelta = profitDelta
            minDeltaMonth = rowData[0]
            maxDeltaMonth = rowData[0]
        
        totalchange = totalchange + profitDelta
        previousmonthprofits = currentmonthprofits
        
        # If current profits is bigger than last seen biggest current profits than current profits is max
        if profitDelta > maxProfitDelta:
            maxProfitDelta = profitDelta
            maxDeltaMonth = str(rowData[0])
        if profitDelta < minProfitDelta:
            minProfitDelta = profitDelta
            minDeltaMonth = str(rowData[0])
    
    averagechange = totalchange / (totalmonths - 1)
    
# Print results

# Assign results to list
lines = [
    f"Financial Analysis",
    f"----------------------------------",
    f"Total Months: {str(totalmonths)}",
    f"Total: ${str(totalprofits)}",
    f'Average Change: ${"{:.2f}".format(averagechange)}',
    f"Greatest Increase in Profits: {str(maxDeltaMonth)}: (${str(maxProfitDelta)})",
    f"Greatest Decrease in Profits: {str(minDeltaMonth)}: (${str(minProfitDelta)})",
]

# Assign variable to list to print
outputString = '\n'.join(lines)

# Print to terminal
print(outputString)

# Open path to text file
path_results = os.path.join('.', 'Analysis', 'PyBankResults.csv')

# Write in text file
with open(path_results, 'w') as f:
    f.writelines(outputString)