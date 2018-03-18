import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
from Figures import figure_1
from Figures import figure_2
from Figures import figure_3
from Figures import table_3
from Figures import Gantt_Chart_1

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

GDP = quandl.get("FRED/GDP", authtoken = "EvzHu2GEhMsgyzCTaFz6")
Google = quandl.get("WIKI/GOOGL", authtoken = "EvzHu2GEhMsgyzCTaFz6")
Apple = quandl.get("WIKI/AAPL", authtoken = "EvzHu2GEhMsgyzCTaFz6")
Intel = quandl.get("WIKI/INTC", authtoken = "EvzHu2GEhMsgyzCTaFz6")
Oracle = quandl.get("WIKI/ORCL", authtoken = "EvzHu2GEhMsgyzCTaFz6")
Adobe = quandl.get("WIKI/ADBE", authtoken = "EvzHu2GEhMsgyzCTaFz6")
	



app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title="khovhannisyan reactive dashbards"
app.layout=html.Div([
	#row 1
	html.Div([ 	

		html.H1(children="Homework 5", style={"color":"darkred", "text-align":"center", "font-family":"cursive",})],
		className="twelve columns"),

		html.Div([
			html.Div([ 
				dcc.RadioItems(
      			id='radio',
        			options=[
            {"label":'Employee Churn', "value":"figure_1"},
            {"label":'Startup RoadMap', "value":"Gantt_Chart_1"}])	
				], className="two columns"),


			html.Div([
			dcc.Graph(id="Graph")],
			className="ten columns"),


			], className="twelve columns"),
		
#row 2
		html.Div([
			html.Div([dcc.Dropdown(id = 'option_in', options=[
	            {'label': 'Google', 'value': 'Google'},
	            {'label': 'Apple', 'value': 'Apple'},
	            {'label': 'Intel', 'value': 'Intel'},
	            {'label': 'Oracle', 'value':'Oracle'},	
	            {'label': 'Adobe', 'value': 'Adobe'}
            ], placeholder='Select stocks...', multi=True),

            html.Button(id='submit',n_clicks=0, children='Submit'),
    
				], className="two columns"),	
			html.Div([
					dcc.Graph(id="Graph2")],
					className="six columns"),

			html.Div([
					dcc.Graph(id="table")],
					className="four columns"),
	

			], className="twelve columns"),
#row 3
		html.Div([
			html.Div([dcc.RangeSlider(id = 'slider', min=0, max=len(GDP.index), value=[0, len(GDP.index)])],
			className="four columns"),

			html.Div([dcc.Graph(id="Graph3")],
			className="eight columns"),
			
			], className="twelve columns")
		
		])
#radio butons
@app.callback(
    Output(component_id='Graph', component_property='figure'),
    [Input(component_id='radio', component_property='value')])
    
def update_graph(input_value_1):
    figure=eval(input_value_1)
    return figure


#dropdown
@app.callback(
    Output(component_id='Graph2', component_property='figure'),
    [Input(component_id='submit', component_property="n_clicks")],
    [State(component_id='option_in', component_property='value')]
)

def update_stock(clicks, input_value_2):
	stock_data_1 = eval(input_value_2[0])
	stock_data_2 = eval(input_value_2[1])
	stock_data_1["Percent_Change"]=stock_data_1.Open.pct_change()
	stock_data_2["Percent_Change"]=stock_data_2.Open.pct_change()
	trace_s_1 = go.Box(x=stock_data_1["Percent_Change"], name=input_value_2[0])
	trace_s_2 = go.Box(x=stock_data_2["Percent_Change"], name=input_value_2[1])
	layout_2 =dict(title = "<i>Distribution of price changes of </i>"+input_value_2[0]+" and "+input_value_2[1])
	data = [trace_s_1, trace_s_2]
	figure = dict(data=data, layout=layout_2)
	
	return figure
	#table
@app.callback(
    Output(component_id='table', component_property='figure'),
    [Input(component_id='submit', component_property="n_clicks")],
    [State(component_id='option_in', component_property='value')]
)

def update_stock_table(clicks, input_value_3):
	stock_data_1_t = eval(input_value_3[0])
	stock_data_2_t = eval(input_value_3[1])
	stock_data_1_t["Percent_Change"]=stock_data_1_t.Open.pct_change()
	stock_data_2_t["Percent_Change"]=stock_data_2_t.Open.pct_change()
	stock_data_1_tb=stock_data_1_t.iloc[1:5,-1:].round(3)
	stock_data_2_tb=stock_data_2_t.iloc[1:5,-1:].round(3)
	table_header= dict(values=[input_value_3[0],input_value_3[1]], align=["left", "center"], font=dict(color="white", size=12), fill=dict(color="blue"))
	append_tables=dict(values=[stock_data_1_tb.values, stock_data_2_tb.values], align=["left", "center"], fill=dict(color=["yellow", "white"]))
	trace_table=go.Table(header=table_header, cells=append_tables)
	data_table=[trace_table]
	table_layout=dict(width=500, height=300)
	table=dict(data=data_table, layout=table_layout)
	return table

#slider
@app.callback(
    Output(component_id='Graph3', component_property='figure'),
    [Input(component_id='slider', component_property='value')]
)
def update_graph_slider(input_value3):

	index_x = GDP.index[input_value3[0]:input_value3[1]]
	values_y = GDP.Value[input_value3[0]:input_value3[1]]

	trace_scatter = [go.Scatter(x=index_x,y=values_y,fill="tozeroy")]
	layout_gdp = dict(title = '<b>US GDP over time</b>')
	figure_3 = dict(data=trace_scatter, layout = layout_gdp)
	return figure_3


if __name__=='__main__':
	app.run_server(debug=True)



		