#Logan H's Monthly Tax Finder

#PSUEDO CODE:

# 1) Set up Def function
# 2) Set the tax rates (State_Tax = .05, County_Tax = .025)
# 3) Set up formulas for taxes and total, return taxes/total
# 4) Ask (float input) total monthly sales
# 5) Calculate all the taxes
# 6) Print all the taxes


# 1)
def calculate(total_sales):
# 2)
    S_T_R = .05
    C_T_R = .025

# 3)
    state_tax = total_sales * S_T_R
    county_tax = total_sales * C_T_R
    total_tax = state_tax + county_tax

    return state_tax, county_tax, total_tax

# 4)
sales = float(input("How much did you make in monthly sales? "))

# 5)
state_tax, county_tax, total_tax = calculate(sales)

# 6)
print(f"The state tax is ${state_tax:.2f}")
print(f"The county tax is ${county_tax:.2f}")
print(f"The total sales tax is ${total_tax:.2f}")
