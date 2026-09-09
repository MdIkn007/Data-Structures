marks, att, income = map(float, input().split())
print("Eligible" if (marks >= 85 and att >= 75 and income <= 300000) else "Not Eligible")
