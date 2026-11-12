# Self-Assessment Questions
# 1. Python is easier to automate cleaning/managing data but if you have a lot of files then Excel is easier to quickly look at, change and create charts.
# 2. An example of a business that could use an append mode log would be to keep track of daily sales. This is useful as you can add more entries without losing old entries.

import csv
from datetime import datetime

# Exercise 2: Read and print raw rows
print("Exercise 2: Raw Rows")
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Skip the header
print("\nExercise 3: Skip Header")
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4: Compute totals
print("\nExercise 4: Compute Totals")
total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")

# Exercise 5: Filter and write
print("\nExercise 5: Filter and Write")
original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, f"{total:.2f}"])
                cleaned_count += 1

print(f"Original rows: {original_count}")
print(f"Cleaned rows: {cleaned_count}")

# Exercise 6: csv.DictReader
print("\nExercise 6: DictReader")
dict_total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${dict_total_revenue:.2f}")

# csv.reader uses column positions to access values.
# csv.DictReader uses column names, which makes the code easier to read.

# Exercise 7: Sales summary by product
print("\nExercise 7: Sales Summary")
sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

# Exercise 8: Append mode log
print("\nExercise 8: Append Mode Log")

with open("data/run_log.txt", "a") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

print("Run log updated.")
