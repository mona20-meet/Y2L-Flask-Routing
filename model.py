
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Product:
    def __init__(self, id, name, price, picturelink, discription):

        self.id = id 
        self.name = name
        self.price = price
        self.picturelink = picturelink
        self.discription = discription




class Product(Base):
   __tablename__ = 'product'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
   picturelink = Column(String)
   discription = Column(String)


class Cart(Base):
   __tablename__ = 'Cart'
   id = Column(Integer, primary_key=True)
   productID = Column(Integer)