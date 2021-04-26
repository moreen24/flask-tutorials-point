from flask import Flask
app=Flask(__name__)

app.route('/produts<name>')
def get_products(name):
    return "the product name is " + str(name)