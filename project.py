from flask import Flask, render_template
import restaurant_dao 

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id): # should match with paramter of url accordingly.
    restaurant = restaurant_dao.get_restaurant(restaurant_id)
    items = restaurant_dao.get_menu(restaurant_id)

    return render_template('menu.html', restaurant = restaurant, items = items)

@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    pass

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    pass

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(host = '', port = 5000)