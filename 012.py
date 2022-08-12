import pandas as pd
import matplotlib.pyplot as plt

Production_Data = pd.DataFrame({'Year':['2003','2005','2007','2009','2011','2013','2015','2017','2019','2021'], 'Production':[7,4,9,19,23,4,16,8,6,25]})
x = Production_Data.Year
y = Production_Data.Production
plt.scatter(x, y)
plt.show()
