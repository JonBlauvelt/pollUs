import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask.ext.socketio import SocketIO, emit, disconnect #import socketio things
from flask_socketio import join_room, leave_room, disconnect #import socketio room things
from flask.ext.login import LoginManager

import psycopg2
import psycopg2.extras


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
app.secret_key = os.urandom(24).encode('hex')
login_manager = LoginManager()
login_manager.init_app(app)

#create socketio app - pass in the flask app created above
socketio = SocketIO(app)

@socketio.on('connect', namespace='/poll')
def makeConnection():
    print('connected')

#when someone first lands
@app.route('/')
def mainIndex():
    print 'in hello world'
    return app.send_static_file('index.html')
    
# start the server - change to socketio
if __name__ == '__main__':
        socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 80)), debug=True)
