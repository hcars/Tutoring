import random
#There are several bugs below it is your job to find them
#Generate random list
list = []
for i in range(20):
    list.append(random.randint(-100, 100))
#Sort it by ascending value
#bubble-sort algorithm below
#You can see an animation of this algorithm at http://www.cs.armstrong.edu/liang/animation/web/BubbleSort.html
def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j] = temp
    return list            
#Now take the absolute value
for k in list:
    k = abs(k)
#Now sort the absolute values
bubbleSort(list)
#Estimating square root
#This uses a sequence to find sqrt(2) repeating the process a certain number of times
#More info. below:
#https://math.stackexchange.com/questions/1571311/calculating-square-roots-using-the-recurrence-x-n1-frac12-leftx-n-fr
def root2(iterations):
    x1 = 2
    for i in range(iterations):
            newVal = .5 *(x1 + (2/ x1))
            x = newVal
    return x
root2(1000)