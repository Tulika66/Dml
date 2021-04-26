#FLASK_APP=api3.py flask run --port 5001

from flask import Flask, request
from flask_restful import Resource, Api
from math import exp as exp 

app = Flask(__name__)
api = Api(app)

# Calculate neuron activation for an input
def activate(weights, inputs):
	if(inputs==None):
		inputs=0
	activation = float(weights[-1])
	for i in range(len(weights)-1):
		activation += float(weights[i]) * float(inputs[i])
	return activation
 
# Transfer neuron activation
def transfer(activation):
	return float(1.0 / float(1.0 + exp(-activation)))
        

@app.route('/forward')
def forward():
	query = request.args.to_dict(flat = False)
	weights = query['weights']
	inputs = query['inputs']
	activation = activate(weights,inputs)
	message = transfer(activation)

	return str(message)


if __name__ == '__main__':
    app.run(debug=True)