import pandas as pd
#DataFrame with details BookID, Book Description, Author, Publisher,Quantity and Price
Booking_Data = pd.DataFrame([['B001','Veer',4,100,'Manish'],['B002','Umesh',2,200,'Kishor'],['B003','Lavanya',6,150,'Manish'],['B004','Shobhana',5,250,'John'],['B005','Piyush',3,100,'Kishor']], columns=['Booking Code','Customer Name','No of Ticket','Ticket Rate','Booking Clerk'])
print(Booking_Data)


#b) Add a new row with values ( B006 , Vijay, 7, 150, John)
Booking_Data.loc[len(Booking_Data.index)] = ['B006','Vijay',7,150,'John']

print("print NEW Booking Data:")
print(Booking_Data)


Total_Amount=[]
for index, row in Booking_Data.iterrows():
    Total_Amount.append(int(row['No of Ticket'])*int(row['Ticket Rate']))
#a) Add column "Total Amount" that calculates total amount of tickets and assign that to new column.
Booking_Data['Total_Amount'] = Total_Amount
print("print NEW DataFrame with Total_Amount:")
print(Booking_Data)
