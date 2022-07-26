import pandas as pd
import openpyxl

stock_names = []
stock_shares = []

while 1:
    name = input("Enter the bought stock")
    if name == 'q':
        break
    stock_names.append(name)
    shares = int(input("Enter the number of shares bought"))
    stock_shares.append(shares)



df = pd.DataFrame([stock_shares],index=['July'],columns=stock_names)
df.to_excel('crap_test.xlsx',sheet_name="crap")