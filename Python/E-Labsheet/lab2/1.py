inc = float(input(""))
ex = float(input(""))

profit = inc + ex

profitdone = f"{profit:08.2f}"

print(f"Total Income {inc:>+8.2f} bahts")
print(f"Expense {ex:>13.2f} bahts")
print(f"Profit {profitdone:>14} bahts")


