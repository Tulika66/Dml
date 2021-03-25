import json
from math import exp
from flask import Flask,request
from flask_restful import Resource, Api
import requests
from time import sleep


# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = float(weights[-1])
	for i in range(len(weights)-1):
		activation += float(weights[i]) * float(inputs[i])

	return activation
 
# Transfer neuron activation
def transfer(activation):
	return ((1.0) / (1.0 + exp(-activation)))

app = Flask(__name__)
api = Api(app)

# ,methods=['GET']
@app.route('/childcompute')  
def childcompute():

		# weights=request.args['weights']
		query_param=request.args.to_dict(flat=False)
		weights=query_param['weights']
		inputs=query_param['inputs']
	
		activation=activate(weights,inputs)
		# message=activation
		message=transfer(activation)
		sleep(9)
		return str(message)




if __name__ == '__main__':
	app.run(debug=True)
	