from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('add_mul.html')

@app.route('/empty-value')
def empty_value():
   return 'you are not sending any values!!!'

@app.route('/operation', methods = ['POST', 'GET'])
def operation():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']

        if a == "" and b == "":
            return redirect(url_for('empty_value'))
       
        add_val = int(a) + int(b)
        print("addition: ", add_val)

        mul_val = int(a) * int(b)
        print("multiplication: ", mul_val)

        return f"addition is: {add_val}   multiplication is :{mul_val}"
    
if __name__ == '__main__':
    app.run(host ="0.0.0.0", port = 5001 ,debug = True)