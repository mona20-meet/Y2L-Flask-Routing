from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product( name, price, picturelink, discription):

    product_object = Product(
        name=name,
        price=price,
        picturelink=picturelink,
        discription=discription
        )
    session.add(product_object)
    session.commit()
def edit_product(id,name, price, picturelink, discription):
	product_object= session.query(Product).filter_by(id=id).first()
	product_object.name = name
	product_object.price=price
	product_object.picturelink=picturelink
	product_object.discription=discription


	session.commit()

def delete_product(id):
	session.query(Product).filter_by(id=id).delete()
	session.commit()
def return_all_product():
	product = session.query(Product).all()
	return product 
def return_product(id):
	session.query(Product).filter_by(id=id)
	return product
def Add_To_Cart(productID):
    cart_object = Cart(
        productID=productID
        )
    session.add(Cart)
    session.commit()
	



add_product('snake',19.99 ,'https://github.com/mona20-meet/Y2L-Flask-Forms.git','this is a pretty good snakey snake')