import pandas
from datetime import datetime as dt
# import plotly.plotly as py
import plotly.offline as po
import plotly.graph_objs as go

df1 = pandas.read_csv("sample.csv")

time = list(df1.iloc[0:95, 0])
data = list(df1.iloc[0:95, 1])

trace = go.Scatter(x=time, y=data)

data1 = [trace]

po.plot(data1, filename="/Users/ahanjrah/git/python3/scripts/license-usage-" + str(dt.now().month) + str(dt.now().day) + str(dt.now().year) + ".html")
# py.iplot(data1, filename='basic-line')
