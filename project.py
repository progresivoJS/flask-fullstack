from flask import Flask
from database_setup import Restaurant, MenuItem
import restaurant_dao 

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    items = restaurant_dao.get__menu_items_of_first_restaurant()

    output = ''
    for item in items:
        output += item.name + "</br>"
        output += item.price + "</br>"
        output += item.description + "</br>"
        output += "</br>"
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '', port = 5000)