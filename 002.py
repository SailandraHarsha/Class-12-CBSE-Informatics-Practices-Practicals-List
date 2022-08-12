from numpy import *
arr = array([])
#accept number of subjects from user
n = int(input("Enter the number of subject(s) values you want:  "))

#accept marks from all subjects from user
for i in range(n):
    v = input("Enter Marks in subject "+str(i+1)+" :  ")
    arr = append(arr, int(v))

print("All Marks entered: ")
print(arr)

sum = 0
avg = 0
perc = 0

#calculate sum of all marks
for j in range(0, len(arr)): 
    sum = sum + arr[j]

#print Sum
print("Sum of all marks: ",str(sum))
#Calculate and print Average marks
print("Average marks: ",str(sum/len(arr)))
#Calculate and print Percentage
print("Percentage: ",str((sum/(100*len(arr)))*100))
