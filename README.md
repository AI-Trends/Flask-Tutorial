# Flask-Tutorial
GOAL :- Using Flask web application framework to serve as API request and deploy your application in global and production.

## Flask Introduction

* Importing flask module in the project is mandatory. 
1. from flask import Flask

* Flask constructor takes the name of current module (__name__) as argument.
2. app = Flask(__name__)

* The route() decorator in Flask is used to bind URL to a function which tells the application which URL should call the associated function.
3. app.route(rule, options)

rule parameter: represents URL binding with the function.
options: GET, POST methods to receive input objects and send output objects.

* Different methods of data retrieval from specified URL are defined in HTTP protocol.

#### Methods & Description 

* GET : Sends data in unencrypted form to the server. Most common method.
* HEAD: Same as GET, but without response body
* POST: Used to send HTML form data to server. Data received by POST method is not cached by server.
* PUT : Replaces all current representations of the target resource with the uploaded content.
* DELETE : Removes all current representations of the target resource given by a URL

#### attributes of request object 

* Form − dictionary object containing key and value pairs of form parameters and their values.
* args − parsed contents of query string which is part of URL after question mark (?).
* Cookies − dictionary object holding Cookie names and values.
* files − data pertaining to uploaded file.
* method − current request method.

* url_for() function : very useful for dynamically building a URL for a specific function. first argument : the name of a function. remaining arguments: each corresponding to the variable part of URL.

* redirect() function: redirect current url to specific function url


### step 1: Create Virtual Envrionment and Install Requirements

* virtualenv --python=python3.6 env

* source env/bin/activate

* pip install -r requirements.txt

### step 2: simple example 
* python3 addition_multiplication_flask.py

### step 3: Using Advance REST Client to Test Webserver request and response

* Advance REST Client POST request check
* Chrome extention: add Advance REST Client extention in your browser
* Open Advance REST Client
* Select Request Method: POST
* Add Request URL: http://127.0.0.1:5001/operation
* Goto Body part 
* Select Content type: Form data
* and Add Form data parameters: a and b.

### step 4: Rendering Dynamic Webpages using Zinja-2 template
Format:
 * ---/addition_multiplication_flask.py 
 * ---/templates
 * -------/add_mul.html

Run 
* python3 addition_multiplication_flask.py

### step 5: hosting web application in global domain
download ngrok
* https://ngrok.com/download

give which port you assign in your web server
* ./ngrok http 5001

change Url
* http://localhost:5001 -> https://d9233c34.ngrok.io

### step 6: Dog - Cat classifier
* git clone https://github.com/ardamavi/Dog-Cat-Classifier.git

already done below steps
* cd Dog-Cat-Classifier/
* pip install -r requirements.txt
* cd ../Dog-Cat-Classifier

Run WebServer for Dog-Cat Classifier

* python3 Dog-Cat-Classifier_server.py 

