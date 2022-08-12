import pandas as pd
import matplotlib.pyplot as plot

#Read data from open source (e.g. data.gov.in)
df = pd.read_csv('011.csv',sep=',');
print('Orignal dataframe:')
#print Orignal dataframe
print(df)
print('aggregate:')
#calculate and print aggregate
print(df.aggregate(['sum', 'min']))

x = df.State_Name
y = df.Population_2011
plot.scatter(x, y)
plot.show()
