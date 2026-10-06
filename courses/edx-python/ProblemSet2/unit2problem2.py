monthlyInterestRate = annualInterestRate / 12.0
payment = 10

while True:
    remaining_balance = balance

    for month in range(12):
        unpaid_balance = remaining_balance - payment
        remaining_balance = unpaid_balance + (monthlyInterestRate * unpaid_balance)

    if remaining_balance <= 0:
        break
    else:
        payment += 10
