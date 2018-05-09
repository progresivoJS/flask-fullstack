from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

def get_restaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    return restaurant

def get_menu(restaurant_id):
    '''
    return restaurant_id's menu.
    '''
    restaurant = get_restaurant(restaurant_id)
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return items

def add_new_item(name, restaurant_id):
    newItem = MenuItem(name = name, restaurant_id = restaurant_id)
    session.add(newItem)
    session.commit()
    return