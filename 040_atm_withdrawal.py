balance, withdraw, min_bal = map(float, input().split())
if balance - withdraw >= min_bal:
    print(f"Approved. New Balance: {balance - withdraw}")
else:
    print("Rejected. Insufficient minimum balance.")
