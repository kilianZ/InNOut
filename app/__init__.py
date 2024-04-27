from flask import Flask 

# create flask app
app = Flask(__name__) 
app.secret_key = "super secret key"

# Import routes after app is created to avoid circular imports 
from . import routes 

# Optionally, set up database here 

# Other setups like login management, mail, etc. 
