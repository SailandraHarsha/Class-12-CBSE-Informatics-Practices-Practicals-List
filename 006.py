import pandas as pd
#reads Employee Data (Employee No, Name, Address, Date of Joining, Salary) from CSV
emp_data = pd.read_csv('006.csv')
#displays the details
print(emp_data.head())
