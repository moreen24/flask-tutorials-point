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

if __name__ == '__main__':
   app.run()

