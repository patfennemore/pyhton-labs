'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

input_investment_amount = float(input("Please enter investment amount: "))
input_interest_rate = float(input("Please enter interest rate in percentage: "))
input_investment_years = float(input("Please enter the numbers of years to invest: "))

input_interest_rate_decimal = input_interest_rate/100

future_value = (input_investment_amount*(1+input_interest_rate_decimal)**input_investment_years)

print(future_value)