
import socket
import json
from math import exp
#receive -:loads
#send    -:dumps

message_check="begins"

# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation
 
# Transfer neuron activation
def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # take input

   # message_check.lower().strip() != 'bye'
    while True:
        # data_loaded = json.loads(data) #data loaded

       
        data = client_socket.recv(1024).decode('utf-8')  # receive response
        
        if(data=='bye'):
            break

        data=json.loads(data)
        # data_close_check=json.dumps(data)
        

        print('Received from server: ' + str(len(data)))  # show in terminal
        # message_check=json.loads(data)

        weights=data['weights']
        inputs=data['inputs']
        activation=activate(weights,inputs)
        message=transfer(activation)
        message = json.dumps(message)
        client_socket.send(message.encode('utf-8'))  # send message
        print("Sending calcualted message to server \n")

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
