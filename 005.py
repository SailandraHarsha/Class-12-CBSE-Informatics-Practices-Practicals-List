import pandas as pd
print("initialize list of lists:")
dict = {'Product':['CPU', 'Mouse', 'Keyboard', 'Printer','Hard_Disk','Plotter'],
        'Company':['Compaq', 'Dell', 'HP', 'Epson','Toshiba','Sony'],
        'Quantity':[40,20,15,5,10,5],
        'Price':[900,500,500,5700,2000,8000]
       }
print("Create the pandas DataFrame:")
df = pd.DataFrame(dict)
print("print DataFrame:")
print(df)

#b) Add a new row to the DataFrame with Data – (Scanner, HP, 2, 9500)
df.loc[len(df.index)] = ['Scanner', 'HP', 2, 9500]

print("print NEW DataFrame:")
print(df)

Total_Price=[]
for index, row in df.iterrows():
    Total_Price.append(int(row['Quantity'])*int(row['Price']))
#a) Add a new column Total Price that contains Total Price of Product (Total Price = Quantity * Price)
df['Total_Price'] = Total_Price
#c) Display the Product and Total Price of the DataFrame.
print("print NEW DataFrame with Total_Price:")
print(df)
