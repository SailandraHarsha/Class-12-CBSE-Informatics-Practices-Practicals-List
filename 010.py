import pandas as pd
import matplotlib.pyplot as plot

# A python dictionary
data = {"Subject":['Accountancy','Biology','Biotechnology','Business Studies','Chemistry','Computer Science','Economics','Geography','History','Informatics Practices','Mathematics','Applied Mathematics','Physics','Political Science','Psychology','Sociology'],"Marks/Grades":[95,92,88,96,78,99,89,87,82,80,97,90,84,89,90,77]};

# Dictionary loaded into a DataFrame
dataFrame = pd.DataFrame(data=data);

# Draw a vertical bar chart
dataFrame.plot.bar(x="Subject", y="Marks/Grades", rot=70, title="Different subject of Class 12 - Year 2021-2022");
plot.show(block=True);
