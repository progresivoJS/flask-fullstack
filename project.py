from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
import restaurant_dao 

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id): # should match with paramter of url accordingly.
    restaurant = restaurant_dao.get_restaurant(restaurant_id)
    items = restaurant_dao.get_menus_of_restaurant(restaurant_id)

    return render_template('menu.html', restaurant = restaurant, items = items)

@app.route('/restaurants/<int:restaurant_id>/new/', methods = ['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        restaurant_dao.add_new_item(request.form['name'], restaurant_id)
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id = restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    if request.method == 'GET':
        menu = restaurant_dao.get_menu(menu_id)
        return render_template('editmenuitem.html', menu = menu)
    else:
        restaurant_dao.rename_item(menu_id, request.form['name'])
        flash("Menu Item Edited")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods = ['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if request.method == 'GET':
        item = restaurant_dao.get_menu(menu_id)
        return render_template('deletemenuitem.html', item = item)
    else:
        restaurant_dao.delete_item_from_restaurant(restaurant_id, menu_id)
        flash("Menu Item Deleted")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))

# Making an API Endpoint (GET Request)
@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def restaurantMenuJSON(restaurant_id):
    items = restaurant_dao.get_menus_of_restaurant(restaurant_id)
    return jsonify(MenuItems = [i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def get_menu(restaurant_id, menu_id):
    item = restaurant_dao.get_menu(menu_id)
    return jsonify(MenuItem = item.serialize)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '', port = 5000)