import os
import csv

# Set the path for the csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")


# Initialize the variables to hold data
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
profitloss_changelist = []
month_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 10000000000]


# with open as csvfile
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Read through each row of data afer the header
    for row in csvreader:

        # Keep track of all counted months
        total_months = total_months + 1

        # Calculation needed for profit loss
        total_profit_loss += int(row[1])

        # Calculation in profit loss change between current and previous rows 
        profit_loss_change = int(row[1]) - prev_profit_loss
        profitloss_changelist.append(profit_loss_change)
        prev_profit_loss = int(row[1])

        # Find greatest increase in Profits (date/amount)
        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # Find greatest decrease in loss (date/amount) 
        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculation needed for average change (Profit/loss)
profitloss_changelist.pop(0)
average_change = round(sum(profitloss_changelist)/(total_months-1), 3)

# Print the financial analysis to the console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Print out .txt file capturing analysis
with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("Total Months: " + str(total_months) + "\n")
    text.write("Total Profits: " + "$" + str(total_profit_loss) +"\n")
    text.write("Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("Greatest Increase in Profits: " + str(greatest_increase) + " ($" + str(greatest_increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(greatest_decrease) + " ($" + str(greatest_decrease) + ")\n")
    text.write("----------------------------------------------------------\n")