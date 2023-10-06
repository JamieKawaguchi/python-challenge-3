
import os
import csv

budget_data= os.path.join ("Documents", "Bootcamp", "python-challenge", "PyBank", "Resources", "budget_data.csv")

with open (budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)

    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    monthly_changes = []
    months = []


    for row in csv_reader:
        total_months += 1
        current_profit_loss = int(row[1]) 
        net_total += current_profit_loss

        if total_months > 1:
                    
            change = current_profit_loss - previous_profit_loss
            monthly_changes.append(change)
            months.append(row[0])  
        previous_profit_loss = current_profit_loss

    average_change = sum(monthly_changes) / len(monthly_changes)

    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    increase_index = monthly_changes.index(greatest_increase)
    decrease_index = monthly_changes.index(greatest_decrease)

    greatest_increase_month = months[increase_index]
    greatest_decrease_month = months[decrease_index]  

    print(f"Financial Analysis")
    print(f"-----------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")






