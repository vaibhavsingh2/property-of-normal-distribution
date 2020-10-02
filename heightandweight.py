import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
height_list=df["Height(Inches)"].to_list()

weight_list = df["Weight(Pounds)"].to_list()

height_mean = statistics.mean(height_list)
height_mode = statistics.mode(height_list)
height_median = statistics.median(height_list)

weight_mean = statistics.mean(weight_list)
weight_median = statistics.median(weight_list)
weight_mode = statistics.mode(weight_list)

print(height_mean)
print(height_mode)
print(height_median)

print(weight_mean)
print(weight_mode)
print(weight_median)

fig=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"], show_hist=False)
fig.show()

fig1=ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"], show_hist=False)
fig1.show()
