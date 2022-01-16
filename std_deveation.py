import csv
import math 
import pandas as pd
import plotly.express as px
df=pd.read_csv('data.csv')

with open('data.csv', newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]
fig = px.scatter(df, x='student Number', y='Marks')
fig.update_layout(shapes=[
dict(
    type='line',
    y0=mean, y1=mean,
    x0=0, x1=total_entries
)])
fig.update_yaxis(rangemode='2zero')
fig.show()
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)
    mean=total/n
    return mean 