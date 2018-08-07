import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('result.csv')

modelversion='1'

app.layout=html.Div(children=[

	html.H1('House Price Prediction with Model Version'+modelversion),
	#dcc.Checklist(
	 #   options=[
	 #       {'label': 'Palo Alto', 'value': 'PA'},
	 #       {'label': 'San Jose', 'value': 'SJ'},
	 #   ],
	 #   values=['PA', 'SJ'],
	 #   labelStyle={'display': 'inline-block'}
	#)
	dcc.Graph(
        id='predicthouse',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['state'] == i]['prediction'],
                    y=df[df['state'] == i]['target'],
                    text= df[df['state'] == i]['area'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 10,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df['state'].unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'prediction'},
                yaxis={'title': 'target'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),

	#dcc.Graph(id='example',
			#figure={
				#'data':[
				#	{'x':preditdata_PA,'y':target_PA,'type':'markers','name':'PA'},
				#	{'x':preditdata_SJ,'y':target_SJ,'type':'markers','name':'SJ'}
				#	],
				#'layout':{
				#	'title':'prediction on different areas'

				#	}
			#}),
	html.Div(id='output-container-button',
             children='Please enter your house properties'),
	dcc.Input(
	    placeholder='Enter house area',
	    type='number',
	    value=''
	),
	dcc.Input(
	    placeholder='Enter house age',
	    type='number',
	    value=''
	),
	dcc.Input(
	    placeholder='Enter house type',
	    type='text',
	    value=''
	),

	html.Button('Submit', id='button'),
    html.Div(id='prediction-button',
             children='If the prediction is good? (yes or no)'),


	html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button'),
    html.Div(id='evaluate-button',
             children='If the prediction is good? (yes or no)')


    #dcc.DatePickerRange(
    #id='date-picker-range',
    #start_date=dt(1997, 5, 3),
    #end_date_placeholder_text='Select a date!'
#)




	#dcc.Slider(
	#min=-5,
	#max=10,
	#step=0.5,
	#value=-3,
	#)


	])

@app.callback(
    dash.dependencies.Output('evaluate-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])

def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )



if __name__=='__main__':
	app.run_server(debug=True)