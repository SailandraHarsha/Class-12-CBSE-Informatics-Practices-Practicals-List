import pandas as pd
#DataFrame with details BookID, Book Description, Author, Publisher,Quantity and Price
Employee_Data = pd.DataFrame([['mayur',15,51,5.1,55],['anil',16,48,5.2,25],['viraj',17,49,5.1,71],['viraj',17,51,5.3,53],['mahesh',16,48,5.1,51],['viraj',17,59,5.3,50]], columns=['name','Age','weight','height','runsscored'])
print(Employee_Data)

#a) calculate minimum value for each of the row from subset of dataframe that contains age, weight, height, runsscored
minvalue_series = Employee_Data.min()
print(minvalue_series)

#Get Last 03 Rows
Employee_Data_last_3 = Employee_Data.tail(3)

#b) calculate mean for last 3 rows
df_mean = Employee_Data_last_3[['name','Age','weight','height','runsscored']].mean()
print(df_mean)

#Store the data into a CSV File with name “008.csv”
Employee_Data.to_csv('008.csv')

