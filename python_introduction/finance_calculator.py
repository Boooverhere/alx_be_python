
monthly_income = int(input("Enter your monthly income: "))

total_monthly_expenses = int(input("Enter your total monthly expenses: ")) # type: ignore

monthly_savings = monthly_income - total_monthly_expenses

print(f"Your monthly savings are ${monthly_savings}.")

annual_savings = monthly_savings * 12
intrest = annual_savings * 0.05
projected = annual_savings + intrest 

print(f"Projected savings after one year, with interest, is: {projected}.")