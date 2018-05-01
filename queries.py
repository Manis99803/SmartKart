from app import db
from app.models import User,Product,Supplier,Order,Rating,stock
print("All Users")
p = User.query.filter_by().all()
print(p)
p = Product.query.filter_by().all()
print("All Products")

print(p)

print("All Supplier")
p = Supplier.query.filter_by().all()
print(p)

print("All products which are books")
p = Product.query.filter_by(type = 'books').all()
print(p)

print("brand of jacket")
p = Product.query.filter_by(name = 'jacket').first()
print(p.brand)

print('Orders by mudit')
cid = User.query.filter_by(username = 'Mudit').first()
# print(cid)
p = Order.query.filter_by(User = cid).first()
print(p.price)

print("All ratings of a product")
pid = Product.query.filter_by(name = 'Maths').first()
p = Rating.query.filter_by(Product = pid).all()
print(p[0].stars)
print(p[1].stars)

print("checking the stock")
pi= stock.query.filter_by(prod_id='0106'),all()
print(pi.quantity)
'''
select quantity from stock where prod_id='0106'; /*checking stock*/
select brand from product P where P.id IN (select prod_id from books );	/*brand of all books*/
select brand from product P where P.id IN (select prod_id from clothes );
select brand from product P where P.id IN (select prod_id from electronics );
select avg(price) from product P where  P.id IN(select prod_id from electronics);
select name,type,price from product P,electronics E where P.id=E.prod_id;
select name,brand,type,price from product P,clothes E where P.id=E.prod_id;
select name,brand,type,price from product P,books E where P.id=E.prod_id;
select type,sum(price) as total_price from product P,books E where P.id=E.prod_id group by P.type;
'''

