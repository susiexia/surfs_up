from flask import Flask
#create a new Flask app instance
app = Flask(__name__) # magic method in python

#create Flask routes: two steps
@app.route('/') # define the root of route
def hello_world(): # build a function
    return 'Hello world'


# Then use CMD add this file into SLASK_APP envs variable
# THEN flask run