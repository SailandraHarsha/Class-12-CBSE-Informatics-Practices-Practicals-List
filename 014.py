import numpy as np
import matplotlib.pyplot as plt
 
barWidth = 0.1
fig = plt.subplots(figsize =(20, 12))
 
June = [140,160,140,180,110]
July = [130,200,180,190,160]
Aug = [130,130,130,200,130]
Sept = [190,200,170,120,110]
Oct = [160,170,190,180,170]
Nov = [200,190,180,190,130]

#For Bar Chart Start#
#br1 = np.arange(len(June))
#br2 = [x + barWidth for x in br1]
#br3 = [x + barWidth for x in br2]
#br4 = [x + barWidth for x in br3]
#br5 = [x + barWidth for x in br4]
#br6 = [x + barWidth for x in br5]
 
#plt.bar(br1, June, color ='r', width = barWidth,edgecolor ='grey', label ='June')
#plt.bar(br2, July, color ='g', width = barWidth,edgecolor ='grey', label ='July')
#plt.bar(br3, Aug, color ='b', width = barWidth,edgecolor ='grey', label ='Aug')
#plt.bar(br4, Sept, color ='gold', width = barWidth,edgecolor ='grey', label ='Sept')
#plt.bar(br5, Oct, color ='pink', width = barWidth,edgecolor ='grey', label ='Oct')
#plt.bar(br6, Nov, color ='black', width = barWidth,edgecolor ='grey', label ='Nov')
 
#plt.xlabel('Zone', fontweight ='bold', fontsize = 15)
#plt.ylabel('rainfall', fontweight ='bold', fontsize = 15)
#plt.xticks([r + barWidth for r in range(len(June))],['North', 'South', 'East', 'West', 'Central'])
 
#plt.legend()
#plt.show()
#For Bar Chart End#

#For Line Chart Start#
plt.plot(June, color ='r', label ='June')
plt.plot(July, color ='g', label ='July')
plt.plot(Aug, color ='b', label ='Aug')
plt.plot(Sept, color ='gold', label ='Sept')
plt.plot(Oct, color ='pink', label ='Oct')
plt.plot(Nov, color ='black', label ='Nov')

plt.xlabel('Zone', fontweight ='bold', fontsize = 15)
plt.ylabel('rainfall', fontweight ='bold', fontsize = 15)

plt.legend()
plt.show()
#For Line Chart End#
