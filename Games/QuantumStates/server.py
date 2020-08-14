#!/usr/bin/env python
from flask import Flask, send_file, jsonify, redirect, url_for,request, render_template
import os
from State import State

current = State()
current.new_state()
target =  State()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route('/')
@app.route('/index')
def index():
	current.print_bloch().savefig("static/state.png")	
	return render_template('index.html', lista='', state=current.get_state_string(), ans='')

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
	answer=''
	if(request.form['button'] == 'reset'):
		current.reset()
	elif(request.form['button'] == 'new'):
		current.reset()
		current.new_state()
	elif(request.form['button'] == 'rand'):
		current.reset()
		current.random_state()
	else:
		current.apply_gate(request.form["button"])
		if(current.is_equal(target)):
			answer = 'Congratulations!'
	
	current.print_bloch().savefig("static/state.png")	
	
	return render_template('index.html', lista=current.get_gates(), state=current.get_state_string(), ans=answer)

@app.route('/how_to')
def how_to():
	return render_template('how_to.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
