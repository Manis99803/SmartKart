from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User,Order, Product, Supplier, Shipper, Shipment,Stock,Rating, Cart, Electronics, Clothes,Books,OrderList


@app.route('/')
@app.route('/index')
def index():
    if current_user.is_anonymous:
        flash("Not Logged In")
        return redirect(url_for('login'))
    try:
        orders = Order.query.filter_by(cust_id = current_user.id).all()
    except:
        orders = []
    return render_template('index.html',posts = "Welcome to Smart Kart", orders = orders)


@app.route('/adminResults')
def adminResults():
    x = db.engine.execute("select count(*) as Products,supplier.name from stock,supplier where stock.sup_id = supplier.id group by stock.sup_id").fetchall() #no of products supplied by each supplier
    y = db.engine.execute("select sum(stock.quantity) as Quantity, stock.prod_id from stock group by stock.prod_id").fetchall()
    z = db.engine.execute("select books.name , books.prod_type, product.price,stock.sup_id, stock.quantity as AmountInStock from product inner join books on product.id = books.prod_id inner join stock on books.prod_id = stock.prod_id").fetchall()
    v = db.engine.execute("select count(*) as NumberOfBooks, prod_type from books group by prod_type").fetchall()
    print(x)
    print(z)
    return render_template('adminResults.html', x = x,y=y,z=z,v=v)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, name = form.name.data, phno = form.phno.data, address = form.address.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # print(request.form['username'],request.form['email'])
        # print(form.name.data,form.username.data)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/status', methods=['GET', 'POST'])
def status():
    if current_user.is_anonymous:
        flash("Not Logged In")
        return redirect(url_for('index'))
    if request.method == 'POST':
        oid = request.form['OrderID']
        print(oid)
    try:
        o = Order.query.filter_by(id = oid).first()
        stat = o.status
        print(stat)
    except:
        stat = "  "
    return render_template('Order_Status.html', status = stat)

@app.route('/books', methods = ['GET','POST'])
def books():
    if current_user.is_anonymous:
        flash("Not Logged In")
        return redirect(url_for('index'))
    b = []
    if request.method == 'POST':
        ty = request.form['type']
        mi = request.form['min']
        ma = request.form['max']
        sort = request.form['sort']
        print(mi,ma,ty)
    try:
        if ty == 'all':
            b =Product.query.join(Books, (Books.prod_id==Product.id)).all()
        else:
            if sort == 'a':
                b =Product.query.join(Books, (Books.prod_id==Product.id)).filter_by(prod_type = ty).filter(Product.price > mi).filter(Product.price < ma).order_by(Product.price.asc()).all()
                 
                #print(b['name'])
            else:
                b =Product.query.join(Books, (Books.prod_id==Product.id)).filter_by(prod_type = ty).filter(Product.price > mi).filter(Product.price < ma).order_by(Product.price.desc()).all()
    except:
        b = []
    return render_template('Books.html', books = b)

@app.route('/electronics', methods = ['GET','POST'])
def electronics():
    if current_user.is_anonymous:
        flash("Not Logged In")
        return redirect(url_for('index'))
    b = []
    if request.method == 'POST':
        ty = request.form['type']
        mi = request.form['min']
        ma = request.form['max']
        sort = request.form['sort']
    try:
        if ty == 'all':
            b = Electronics.query.filter_by().all()
            # b =Product.query.join(Electronics, (Electronics.prod_id==Product.id)).all()
            print(b)
        else:
            # b = Electronics.query.filter_by(prod_type = ty).all()
            if sort == 'a':
                b =Product.query.join(Electronics, (Electronics.prod_id==Product.id)).filter_by(prod_type = ty).filter(Product.price > mi).filter(Product.price < ma).order_by(Product.price.asc()).all()
                print(b)
            else:
                b =Product.query.join(Electronics, (Electronics.prod_id==Product.id)).filter_by(prod_type = ty).filter(Product.price > mi).filter(Product.price < ma).order_by(Product.price.desc()).all()
    except:
        b = []
    return render_template('Electronics.html', electronics = b)

@app.route('/clothes', methods = ['GET','POST'])
def clothes():
    if current_user.is_anonymous:
        flash("Not Logged In")
        return redirect(url_for('index'))
    b = []
    if request.method == 'POST':
        ty = request.form['type']
        mi = request.form['min']
        ma = request.form['max']
        sort = request.form['sort']
    try:
        if ty == 'all':
            b =Product.query.join(Clothes, (Clothes.prod_id==Product.id)).all()
        else:
            if sort == 'a':
                b =Product.query.join(Clothes, (Clothes.prod_id==Product.id)).filter_by(prod_type = ty).filter(Product.price > mi).filter(Product.price < ma).order_by(Product.price.asc()).all()
            else:
                b =Product.query.join(Clothes, (Clothes.prod_id==Product.id)).filter_by(prod_type = ty).filter(Product.price > mi).filter(Product.price < ma).order_by(Product.price.desc()).all()
    except:
        b = []
    print(b)
    # print(ty)
    return render_template('Clothes.html', clothes = b)

@app.route('/view', methods = ['GET','POST'])
def view():
    b = []
    if request.method == 'POST':
        ty = request.form['type']
        print(ty)
    try:
        if ty == 'Shipper':
            b = Shipper.query.filter_by().all()
            # a =Product.query.join(Books, (Books.prod_id==Product.id)).filter_by(price > min, price < max)
        else:
            b = Supplier.query.filter_by().all()
    except:
        b = []
    return render_template('View.html', views = b)

# a =Product.query.join(Books, (Books.prod_id==Product.id))
# order_by(Post.timestamp.desc())
@app.route('/addtocart', methods= ['GET','POST'])
def addtocart():
    if request.method == 'POST':
        pid = request.form['data']
        print(pid)
    try:
        # o = Order(cust_id = current_user.id)
        ol = OrderList(p_id = pid, quantity = 1,c_id = current_user.id)
    # db.session.add(o)
    # db.session.commit()
        c = Cart(prod_id = pid, customer_id= current_user.id)
        db.session.add(ol)
        db.session.commit()
        db.session.add(c)
        db.session.commit()
    except:
        pid = "Not Found"

    # print(pid)
    return "Hello"

@app.route('/cart', methods =['GET','POST'])
def cart():
    if current_user.is_anonymous:
        flash("Not Logged In")
        return redirect(url_for('index'))
    cart = Cart.query.filter_by(customer_id = current_user.id).all()
    return render_template('cart.html', cart = cart)

@app.route('/buy', methods = ['GET','POST'])
def buy():
    if current_user.is_anonymous:
        flash("Not Logged In")
        return redirect(url_for('index'))
    p = 0
    # a = Cart.query.filter_by(customer_id = current_user.id).all()
    o = Order(price  = 0,status = "placed", cust_id = current_user.id)
    db.session.add(o)
    db.engine.execute("delete from cart where customer_id = "+str(current_user.id))
    a = OrderList.query.filter_by(c_id = current_user.id).filter_by(used = False).all()
    if a is None:
        flash("Cart is empty")
        return redirect(url_for("index"))
    for i in a:
        print(i)
        i.order_id = o.id
        i.used = True
        print("I oid",i.order_id)
        price = Product.query.filter_by(id = i.p_id).first()
        p += price.price

    o.price = p
    db.session.commit()
    flash("Order Placed")
    return redirect(url_for('index'))
