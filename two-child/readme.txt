1.run the two flask files in different ports and terminals  

command for first child 1 in one terminal : 
export FLASK_APP=child1.py
flask run --port 5001

command for child 2 in other terminal :
export FLASK_APP=child2.py
flask run --port 5002

2.run the server_parent in different terminal 

