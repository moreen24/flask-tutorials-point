from flask import Flask, redirect, url_for
import string, random, request
app = Flask(__name__)

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

@app.route('/')
def index():
   return 'the index'
 

@app.route('/first')
def first_route():
   return redirect('/second')


@app.route('/second')
def second_route():                    
  #name = currently logged in user           
  name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))                                
  return  redirect('/third/' + name)

@app.route('/third/<string:name>')
def third_route(name):
   return 'the name is  ' + name

@app.route('/succes/<name>')
def succes (name):
   return 'welcome %s' % name
@app.route('/login',methods=['POST', 'GET'])
def login ():
   if request.method  == 'POST':
       user = request.form['nm']
       return redirect (url_for('succes',name=user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('succes',name = user))
      


if __name__ == '__main__':
    app.run(debug=True)



