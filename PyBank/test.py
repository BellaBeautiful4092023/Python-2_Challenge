import os
import csv

# Correct the path to the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")
budget_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'budget_data.csv')
file_to_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Analysis', 'financial_analysis.txt')

# Open the CSV file using the correct variable name
print("Budget Results")
print("------------------")

#Initialize lists to store profit and losses and month to month changes
change = []
monthToMonthChange = []
total = 0
months = 0
monthCount = 0
totalVolume = 0
greatestIncrease = 0
bestMonth = ''
greatestDecrease = 0
worstMonth = ''


# Open the CSV file using the correct variable name
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        total = total + int(row[1])
        months = months + 1
print(str("total months") + str(months) + str("months"))
print(str("total") + str(total))
print(str("average change") + str(total/months))
# Open the CSV file using the correct variable name

with open(budget_data_csv, newline='') as csvfile:
   
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")
   

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        monthCount += 1
        totalVolume += int(row[1])
        if int(row[1]) > greatestIncrease:
            bestMonth = (row[0])
            greatestIncrease = int(row[1])
        elif int(row[1]) < greatestDecrease:
            worstMonth = (row[0])
            greatestDecrease = int(row[1])
        change.append(int(row[1]))

# track monthly changes
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthToMonthChange.append(monthlyChange)
       
        #change.append(int(row[1]))
    averageChange = sum(monthToMonthChange) / len(monthToMonthChange)             

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(monthCount))
print("Average Change is: $" + str(round(averageChange, 2)))
print("Total: $" + str(totalVolume))
print("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")


#write output to text file
f = open(file_to_output, "w")
f.write("Financial Analysis\n")
f.write("___________________________________\n")

f.write("Total Months: " + str(monthCount))
f.write("Average Change is: $" + str(round(averageChange, 2)))
f.write("Total: $" + str(totalVolume))
f.write("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
f.write("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")
