#dependicies
import os
import csv 

#loadfiles
dirname = os.path.dirname

BankCSV = os.path.join("budget_data.csv")

# Lists to store data/track?
total_months = 0
total_revenue = 0
prev_revenue = 0 
revenue_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",999999999999999]
revenue_changes = []

# read files
with open(BankCSV, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvreader = list(csvreader)
    #loop thorugh all rows of data
    for row in range(1,len(csvreader)):
        # Add title
        total_months = total_months + 1 

        # Add price
        total_revenue = total_revenue + int(csvreader[row][1])
        
        
                # Keep track of changes
        revenue_change = int(csvreader[row][1]) - prev_revenue
        # print(revenue_change)

        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(csvreader[row][1])
        # print(prev_revenue)

        # Determine the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = str(csvreader[row][0])
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = str(csvreader[row][0])

        # Add to the revenue_changes list
        revenue_changes.append(int(csvreader[row][1]))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)

     print("Financial Analysis")
    print("Total Months" + str(total_months))
    print("Total Revenue:" + "$" + str(total_revenue))
    print("Average Change:" + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")")   

Financial Analysis
Total Months50
Total Revenue:$25628650
Average Change:$479183.45
Greatest Increase: Feb-16 ($1837235)    