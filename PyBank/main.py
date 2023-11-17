import os
import csv

# Correct the path to the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")
budget_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'budget_data.csv')
file_to_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Analysis', 'financial_analysis.txt')

# Open the CSV file using the correct variable name
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    total = 0
    months = 0
    for row in csvreader:
        total += int(row[1])
        months += 1

# Open the CSV file using the correct variable name
with open(budget_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    monthCount = 0
    totalVolume = 0
    greatestIncrease = 0
    bestMonth = ''
    greatestDecrease = 0
    worstMonth = ''
    change = []
    monthToMonthChange = []

    for row in csvreader:
        monthCount += 1
        totalVolume += int(row[1])

        # Track monthly changes
        change.append(int(row[1]))

    # Calculate monthly changes and track corresponding months
    for i in range(len(change) - 1):
        monthlyChange = change[i + 1] - change[i]
        monthToMonthChange.append(monthlyChange)

        # Update bestMonth and worstMonth based on monthly changes
        if monthlyChange > greatestIncrease:
            bestMonth = row[0]
            greatestIncrease = monthlyChange
        elif monthlyChange < greatestDecrease:
            worstMonth = row[0]
            greatestDecrease = monthlyChange

# Calculate average change
averageChange = sum(monthToMonthChange) / len(monthToMonthChange)

# Print the results
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(monthCount))
print("Total: $" + str(totalVolume))
print("Average Change: $" + str(round(averageChange, 2)))
print("Greatest Increase in Profits: " + bestMonth + " ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + worstMonth + " ($" + str(greatestDecrease) + ")")

# Write output to text file
with open(file_to_output, "w") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(monthCount) + "\n")
    f.write("Total: $" + str(totalVolume) + "\n")
    f.write("Average Change: $" + str(round(averageChange, 2)) + "\n")
    f.write("Greatest Increase in Profits: " + bestMonth + " ($" + str(greatestIncrease) + ")\n")
    f.write("Greatest Decrease in Profits: " + worstMonth + " ($" + str(greatestDecrease) + ")\n")
