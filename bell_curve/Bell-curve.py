import random
import plotly.express as py
import plotly.figure_factory as ff
import pandas as p
import csv

sumOf=[]
count=[]

"""with open("C:/Users/aryan/Desktop/coding/Coding (Phython)/bell_curve/data.csv") as f:
    reader= csv.reader(f)
    data = list(reader)
data.pop(0)

for x in range(0,100) :
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    sum = dice1 + dice2 
    sumOf.append(sum)
    count.append(x)

fig = ff.create_distplot([data[1]],["result"])
fig.show()
print(type(data))

#fig =py.bar(x=sumOf,y=count)
#fig.show()
   
print("Dice1" + str(dice1))
print("Dice2" + str(dice2))
"""
file = p.read_csv("C:/Users/aryan/Desktop/coding/Coding (Phython)/bell_curve/data.csv")
fig = ff.create_distplot([file["Height(Inches)"].tolist()],["result"],show_hist=False)
fig.show()

print(file)


