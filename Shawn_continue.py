#
# Shawn, 2026/03/04
# Shawn_continue.py
# Test continue command to skip negative numbers
#

# continue — skip the current iteration
transactions = [200, -50, 450, -30, 1200, 80]

print("Positive transactions only:")
for t in transactions:
    if t < 0:
        continue                      # skip negative entries
    print(f"  ${t:,}")






# Simulate compounding interest until a target is reached
balance = 10_000    # initial investment
rate    = 0.07      # 7 % annual return
target  = 20_000
years   = 0

while balance < target:
    balance *= (1 + rate)
    years   += 1

print(f"Investment doubles in {years} years.")
print(f"Final balance: ${balance:,.2f}")