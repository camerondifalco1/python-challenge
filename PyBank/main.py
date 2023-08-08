import csv

# Set up the file paths
input_file_path = "budget_data.csv"
output_file_path = "budget_data_analysis.txt"

# Initialize variables to store data
total_months = 0
net_total = 0
prev_profit = 0
profit_change_list = []
month_list = []

# Open the input file and read its contents
with open(input_file_path) as input_file:
    csvreader = csv.reader(input_file, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the data
    for row in csvreader:
        # Increment total month count
        total_months += 1

        # Add to net total profit
        net_total += int(row[1])

        # Calculate the change in profit
        profit_change = int(row[1]) - prev_profit

        # Add the profit change to the list
        if total_months > 1:
            profit_change_list.append(profit_change)

        # Set the previous profit to the current profit for the next iteration
        prev_profit = int(row[1])

        # Add the month to the month list
        month_list.append(row[0])

# Calculate the average profit change
avg_profit_change = sum(profit_change_list) / len(profit_change_list)

# Calculate the greatest increase in profit and its corresponding month
max_profit_change = max(profit_change_list)
max_profit_change_month = month_list[profit_change_list.index(max_profit_change) + 1]

# Calculate the greatest decrease in profit and its corresponding month
min_profit_change = min(profit_change_list)
min_profit_change_month = month_list[profit_change_list.index(min_profit_change) + 1]

 #Print results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits: {max_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})")

# Open the output file and write the analysis results to it
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Net Total Profit: ${net_total}\n")
    output_file.write(f"Average Change: ${avg_profit_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {max_profit_change_month} (${max_profit_change})\n")
    output_file.write(f"Greatest Decrease in Profits: {min_profit_change_month} (${min_profit_change})\n")

# Print a message to confirm that the output file was created
print(f"Analysis results written to {output_file_path}")

