from flask import Flask, render_template, url_for, request, redirect
import restaurant_dao 

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id): # should match with paramter of url accordingly.
    restaurant = restaurant_dao.get_restaurant(restaurant_id)
    items = restaurant_dao.get_menu(restaurant_id)

    return render_template('menu.html', restaurant = restaurant, items = items)

@app.route('/restaurants/<int:restaurant_id>/new/', methods = ['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        restaurant_dao.add_new_item(request.form['name'], restaurant_id)
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id = restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "Edit page"

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "HI"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '', port = 5000)