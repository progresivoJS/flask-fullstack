from flask import Flask
import restaurant_dao 

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    items = restaurant_dao.get_menu(restaurant_id)

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