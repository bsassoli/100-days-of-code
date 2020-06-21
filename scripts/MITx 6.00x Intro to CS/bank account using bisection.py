
annualInterestRate = 0.2
monthly_ir = annualInterestRate / 12
balance = 320000
updated = balance
epsilon = 0.01

lower = balance / 12
upper = (balance * (1 + monthly_ir) ** 12) / 12.0
min_fixed = (lower + upper)/2
while abs(updated) > epsilon:
    updated = balance
    for month in range(1, 13):
        monthly_outstanding = updated - min_fixed
        updated = monthly_outstanding + (monthly_ir * monthly_outstanding)
    if abs(updated) < epsilon:
        print(min_fixed)
    else:
        if updated > epsilon:
            lower = min_fixed
        else:
            upper = min_fixed
    min_fixed = (lower + upper)/2
print(abs(updated) >= epsilon)
print(round(min_fixed, 2))
