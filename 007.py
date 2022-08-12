import pandas as pd
#DataFrame with details BookID, Book Description, Author, Publisher,Quantity and Price
Employee_Data = pd.DataFrame([['001', 'Engg Book','Harsha','CDAC','10000','Rs.5000'], ['002', 'Medical Book','Sail','IEEE','1000','Rs.12000'],['003', 'Engg Book','Swati','Google','90000','Rs.15000']], columns=['BookID','Book Description','Author','Publisher','Quantity','Price'])
#Store the data into a CSV File with name “Employee_Data”
Employee_Data.to_csv('Employee_Data.csv')
print('CSV file created with Name: Employee_Data.csv')
