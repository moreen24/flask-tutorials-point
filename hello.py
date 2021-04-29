from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"


@app.route('/home')
def home():
   return "This is home"

@app.route('/produts/<name>')
def get_products(name):
    return "the product name is " + str(name)

@app.route('/create/<first_name>/<last_name>')
def create(first_name=None,last_name=None):
    return 'hello' + first_name +","+ last_name    

@app.route('/flask')
def hello_flask(): 
   return'hello flask'

@app.route('/python/')
def hello_python():
   return 'helo python'

@app.route('/admin')
def hello_admin(admin):
   return'hello admin'

@app.route ('/guest/<guest>')
def hello_guest(guest): 
   return 'hello %s as guest' %guest

@app.route('/user/<name>')
def hello_user(name):
  if name == 'admin':
   return redirect(url_for('hello_admin'))
  else:
     return redirect(url_for('hello_guest',guest=name))
     
if __name__ == '__main__':
    app.run()



