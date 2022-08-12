import pandas as pd

Library  = {
'Bid':['B01','B02','B03','B05','B06'],
'Name':['Wings of Fire','The Monk who sold his Ferrari','You Can Win','Who moved my cheese','Real Success'],
'Author': ['A.P.J Abdul Kalam','Robin Sharma','Shiv Khera','Spenser Jhonson','Pattrick Mather Pike'],
'Price':[450,370,350,450,250],
'Mem_Name':['Pranjal','Kunal','Rajat','Roma','Sia'],
'Issue_Date':['2021-04-11','2021-03-15','2021-04-18','2021-02-27','2021-04-23'],
'Status':['Not Returned','Returned','Not Returned','Returned','Not Returned']}
labels = ['a', 'b', 'c', 'd', 'e']

df = pd.DataFrame(Library ,columns=['Bid','Name','Author','Price','Mem_Name','Issue_Date','Status'])
print("Given Dataframe :\n", df) 

rslt_df = df[df['Price'] > 350]

print('\nResult dataframe :\n', rslt_df)
