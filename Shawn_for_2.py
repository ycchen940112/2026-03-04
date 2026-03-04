#
# Shawn, 2026/03/04
# Shawn_for_2.py
# Use for loop with range function
#

# range() generates a sequence of numbers
# range(start, stop, step)  — stop is exclusive
print("Sales Report — Q1 Weeks")
for week in range(1, 13):          # weeks 1 through 12
    weekly_target = 50_000
    print(f"  Week {week:>2}: Target = ${weekly_target:,}")

print("Sales Report — Q1 Weeks")
for week in range(1, 53):          # weeks 1 through 52
    weekly_target = 50_000
    print(f"  Week {week:>2}: Target = ${weekly_target:,}")