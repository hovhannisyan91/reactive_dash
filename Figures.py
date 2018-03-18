
# coding: utf-8

# In[275]:
from plotly.offline import plot, iplot
import plotly.graph_objs as go

import plotly
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.plotly as py
import quandl


# In[262]:

quandl.ApiConfig.api_key = "EvzHu2GEhMsgyzCTaFz6"
data_f2 = quandl.get("FRED/GDP")
data_f3_1 = quandl.get("WIKI/GOOGL")
data_f3_2=quandl.get("BCHARTS/ABUCOINSUSD")


# In[263]:



Label_1=["X8","X7","X6","X5"]
Label_2=["X4","X3","X2","X1"]


y_values_1 = [20, 15, 50, 15]
y_values_2 = [-35,-10, -50,  -15]

trace_f1 = go.Bar(x=y_values_1, y=Label_1, name="<b>Negative</b>", orientation = 'h', marker = dict(color = "darkred", line=dict(color="black", width=2)))

trace_f2 = go.Bar(x=y_values_2, y=Label_2, name="Positive", orientation = 'h', marker = dict(color = "blue", line=dict(color="black", width=2))) #in order to make identical, it is not an acutal 

layout = dict(barmode = 'group',title="<b>Correlations with employees probability of churn</b>", yaxis=dict(title="Variable"))


merge_1 = [trace_f1, trace_f2]
figure_1 = dict(data=merge_1, layout=layout)



# In[261]:


data_2 = [go.Scatter(x=data_f2.index, y=data_f2.Value, mode="lines", fill="tozeroy")]
layout_2=dict(title="<b>US GDP over time</b>")

figure_2 = dict(data=data_2, layout=layout_2)


# In[258]:


data_f3_1["Percent_Change"]=data_f3_1.Open.pct_change()
data_f3_2["Percent_Change"]=data_f3_2.Open.pct_change()

trace_f3_1 = go.Box(x=data_f3_1["Percent_Change"], name="<b>Google</b>")
trace_f3_2 = go.Box(x=data_f3_2["Percent_Change"], name="<b>Bitcoin</b>")

layout_3 =dict(title = "<i>Distribution of price changes</i>")

data_3 = [trace_f3_2, trace_f3_1]
figure_3 = dict(data=data_3, layout=layout_3)



# In[259]:


data_f3_1_1=data_f3_1.iloc[1:5,-1:].round(3)
data_f3_2_1=data_f3_2.iloc[1:5,-1:].round(3)

table_header= dict(values=["Google","Bitcoin"], align=["left", "center"], font=dict(color="white", size=12), fill=dict(color="blue"))

append_tables=dict(values=[data_f3_1_1.values, data_f3_2_1.values], align=["left", "center"], fill=dict(color=["yellow", "white"]))

trace_table=go.Table(header=table_header, cells=append_tables)
data_table=[trace_table]

table_layout=dict(width=500, height=300)

table_3=dict(data=data_table, layout=table_layout)




# In[296]:


Project=[dict(Task="Task 1", Start="2018-01-01", Finish="2018-01-31", Resource='Idea Validation'),
          dict(Task="Task 2", Start="2018-03-01", Finish="2018-04-15", Resource='Team formation'),
          dict(Task="Task 3", Start="2018-04-15", Finish="2018-09-30", Resource='Prototyping')]


colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(210, 60, 180)'] # i have tried other ways of coloring but showed error, strange

Gantt_Chart_1= ff.create_gantt(Project, colors=colors, title="Startup Roadmap", index_col='Resource', show_colorbar=True)


