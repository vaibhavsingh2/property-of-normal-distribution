import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

sumOfTwoDices=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sumOfTwoDices.append(dice1+dice2)

mean=sum(sumOfTwoDices)/len(sumOfTwoDices)
print(mean)

median=statistics.median(sumOfTwoDices)
mode=statistics.mode(sumOfTwoDices)

print(median)
print(mode)

fig = ff.create_distplot([sumOfTwoDices],["Result"],show_hist = False)
fig.show()
