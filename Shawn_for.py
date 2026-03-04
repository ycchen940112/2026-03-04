#
# Shawn, 2026/03/04
# Shawn_for.py
# To test for loop and print each items 
#

# Iterate over a list of items
products = ["Laptop", "Tablet", "Smartphone", "Moniter"]

for product in products:
    print(f"Processing inventory for: {product}")

# range() generates a sequence of numbers
# range(start, stop, step)  — stop is exclusive
print("Sales Report — Q1 Weeks")
for week in range(1, 13):          # weeks 1 through 12
    weekly_target = 50_000
    print(f"  Week {week:>2}: Target = ${weekly_target:,}")