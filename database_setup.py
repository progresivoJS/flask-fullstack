# Configuration
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# class
class Restaurant(Base):
    # table
    __tablename__ = 'restaurant'
    
    # mapping
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
class MenuItem(Base):
    # table
    __tablename__ = 'menu_item'

    # mapping
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'price' : self.price,
            'course' : self.course
        }

# Configuration
## insert at the end of file ##
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)