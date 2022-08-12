import pandas as pd 

#initialize list of lists
print("initialize list of lists:")
data = [['Software','Micosoft',10000],['Processor','Intel',550000],['Motherboard','Asus',1200000],
['Monitor','LG',15000],['Software','Google',70000],['Processor','Asus',450000],['Motherboard','Intel',200000],['Monitor','Dell',25000]]

#Set column names/header
Col=['Item_Category','Name','Expenditure']

print("Create the pandas DataFrame:")
qrtsales = pd.DataFrame(data,columns=Col)

print("print dataframe:")
print (qrtsales)

qs=qrtsales.groupby('Item_Category') 
print('Result after Filtering Dataframe') 
print(qs['Item_Category','Expenditure'].sum())
