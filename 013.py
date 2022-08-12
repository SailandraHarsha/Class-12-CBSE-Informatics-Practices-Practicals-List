import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'Ronaldo':783,'Pele':767,'Messi':755,'Gerd Muller':735,'Eusebio':623,'Maravilla':575}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Name of Football Players")
plt.ylabel("goals scored in the matches")
plt.title("Football Players and their goals scored in the matches")
plt.show()
