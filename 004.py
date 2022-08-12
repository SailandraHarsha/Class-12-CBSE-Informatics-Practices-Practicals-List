import pandas as pd 

print("initialize array:")
dic={'Class' : ['I','II','III','IV','V','VI','VII','VIII','IX','X'], 'Pass-Percentage': [100,100,100,100,100,100,100,100,100,100]}

print("Create the pandas DataFrame:")
result = pd.DataFrame(dic)
print(result)
print(result.dtypes)
print('Shape of dataframe is:::')
print(result.shape)
