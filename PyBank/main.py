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

    # Profits dictionary where key is month and profits are value
        # Profits = {month : profit}
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
    
    # declare each line in csv as variable 'month'
        # add one for each line, add all row index[1] together

    for rowIndex, rowData in enumerate(csvreader):
        totalmonths = totalmonths + 1
        currentmonthprofits = int(rowData[1])
        totalprofits = totalprofits + currentmonthprofits
        
        if rowIndex == 0:
            previousmonthprofits = currentmonthprofits

        # reinitialize min and max profit delta and months to be the first profit delta
        profitDelta = int(currentmonthprofits) - int(previousmonthprofits)
        if (rowIndex == 1):
            minProfitDelta = profitDelta
            maxProfitDelta = profitDelta
            minDeltaMonth = rowData[0]
            maxDeltaMonth = rowData[0]
        
        totalchange = totalchange + profitDelta
        previousmonthprofits = currentmonthprofits
        # if current profits is bigger than last seen biggest current profits than current profits is max
        if profitDelta > maxProfitDelta:
            maxProfitDelta = profitDelta
            maxDeltaMonth = str(rowData[0])
        if profitDelta < minProfitDelta:
            minProfitDelta = profitDelta
            minDeltaMonth = str(rowData[0])
    
    averagechange = totalchange / (totalmonths - 1)
    # Print results to terminal
lines = [
    f"Total Months: {str(totalmonths)}",
    f"Total: ${str(totalprofits)}",
    f'Average Change: ${"{:.2f}".format(averagechange)}',
    f"Greatest Increase in Profits: {str(maxDeltaMonth)}: (${str(maxProfitDelta)})",
    f"Greatest Decrease in Profits: {str(minDeltaMonth)}: (${str(minProfitDelta)})",
]

outputString = '\n'.join(lines)

# Print to terminal
print(outputString)

# Export to file





