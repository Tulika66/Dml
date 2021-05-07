#FLASK_APP=api3.py flask run --port 5001

from flask import Flask, request
from flask_restful import Resource, Api
from math import exp as exp 
import tracemalloc

memoryuse=0

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
	global memoryuse

	tracemalloc.start()

	query = request.args.to_dict(flat = False)
	weights = query['weights']
	inputs = query['inputs']

	#calculate memory use
	current1, peak1 = tracemalloc.get_traced_memory()

	activation = activate(weights,inputs)
	message = transfer(activation)

	current2, peak2 = tracemalloc.get_traced_memory()
	memoryuse = max(memoryuse, ((current2-current1)/ 10**3))
	
	
	tracemalloc.stop()

	return str(message)

@app.route('/getmemory')
def getmemory():
	#return the memory use to the client program
	return str(memoryuse)


if __name__ == '__main__':
    app.run(debug=True)
