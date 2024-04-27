from flask import Flask, redirect, url_for, request, \
        render_template
from markupsafe import escape 
app = Flask(__name__) 

@app.route('/success/<name>')
def success(name):
    return f'Welcome {escape(name)}'

@app.get('/login')
def get_login_page():
    return render_template('./login.html')

@app.post('/login')
def handle_login():
    username = request.form['username']
    password = request.form['password']
    # check user database 
    authenticated = (username == 'kilian' and password == '123') 
    if authenticated:
        return redirect(url_for('success', name=username)) 
    else: 
        return redirect(url_for('get_login_page')) 

'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return render_template('./login.html')
'''
    

'''
@app.route('/login', methods = ['POST', 'GET']) 
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
'''
if __name__ == '__main__':
    app.run(debug=True)
