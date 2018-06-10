import companydb
import sellerdb
import models as dbHandler
from flask import Flask, flash, render_template, redirect, request, make_response,session,url_for
app = Flask(__name__)


def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        username = request.form['username']
        password= request.form['password']
        if(dbHandler.checkUser(username,password)):
            session['username']=username
            return render_template('buyer.html')
        else:
            return render_template('index.html',error=True)
        return render_template('index.html', error=False)
    else:
        return render_template('index.html')

@app.route('/sell', methods=['GET','POST'])
def sell():
    return render_template('sellerindex.html')



@app.route('/buyer', methods=['GET','POST'])
def buyer():
    if request.method == 'POST':
        itemid=dbHandler.fetchItemId(request.form['product'])
        buylist=companydb.fetchbuy(itemid)
        return render_template('buy.html', buylist = buylist)
    else:
        return render_template('buyer.html')

@app.route('/buy', methods=['GET','POST'])
def buy():
    return render_template('buy.html')

@app.route('/createnew', methods=['POST','GET'])
def createnew():
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		email=request.form['email']
		phone=request.form['phone']
		district=request.form['district']
		session['username']=username
		dbHandler.insertUser(email,username,password,phone,district)
		return redirect(url_for('home'))        



@app.route('/sellerindex', methods=['GET','POST'])
def sindex():
    if request.method == 'GET':
        return render_template('sellerindex.html')

@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    if request.method == 'POST':
        sellerid = 56
        #itemid = companydb.fetchitemid(request.form['category'], request.form['item'])
        companydb.insertproduct(sellerid,request.form['item'], request.form['category'], request.form['quantity'], request.form['unit'])
        return render_template('sellerindex.html')
    else:
        return render_template('addproduct.html')

@app.route('/cropinfo', methods=['GET','POST'])
def cropinfo():
    if request.method == 'POST':
        if(request.form['btnclicked']=="tomato"):
            return redirect('/tomato')
        if(request.form['btnclicked']=="banana"):
            return redirect('/banana')
        if(request.form['btnclicked']=="ladiesfinger"):
            return redirect('/ladiesfinger')
    else:
        return render_template('cropinfo.html')

@app.route('/tomato', methods=['GET','POST'])
def tomatoinfo():
    if request.method == 'GET':
        return render_template('tomato.html')

@app.route('/banana', methods=['GET','POST'])
def bananainfo():
    if request.method == 'GET':
        return render_template('banana.html')

@app.route('/ladiesfinger', methods=['GET','POST'])
def ladiesfingerinfo():
    if request.method == 'GET':
        return render_template('ladiesfinger.html')

@app.route('/orders', methods=['GET','POST'])
def orders():
    if request.method == 'GET':
        sellerid=56
        orderlist = companydb.fetchorders(sellerid)
        return render_template('orders.html', ordlist=orderlist)

@app.route('/accept', methods=['GET', 'POST'])
def accept():
    if request.method == 'POST':
        moveorder(request.form['accept'])
        return redirect('/orders')

@app.route('/reject', methods=['GET', 'POST'])
def reject():
    if request.method == 'POST':
        deleteorder(request.form['reject'])
        return redirect('/orders')

@app.route('/farming', methods=['GET','POST'])
def farming():
    if request.method == 'POST':
        if(request.form['farmbtn']=="fert"):
            return render_template('fert.html')
        if(request.form['farmbtn']=="plant"):
            return render_template('plant.html')
        if(request.form['farmbtn']=="compost"):
            return render_template('compost.html')
    else:
        return render_template('farming.html')

@app.route('/fert', methods=['GET','POST'])
def fertilizers():
    if request.method == 'GET':
        return render_template('fert.html')

@app.route('/plant', methods=['GET','POST'])
def plant():
    if request.method == 'GET':
        return render_template('plant.html')

@app.route('/compost', methods=['GET','POST'])
def compost():
    if request.method == 'GET':
        return render_template('compost.html')

@app.route('/catalog', methods=['GET','POST'])
def catalog():
    if request.method == 'GET':
        sellerid=56
        itemlist=companydb.fetchproducts(sellerid)
        print(itemlist)
        return render_template('catalog.html', catlist=itemlist)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/items', methods=['GET','POST'])
def items():
    if request.method == 'GET':
        return render_template('items.html')

if __name__== '__main__':
    app.run()
