import companydb
from flask import Flask, flash, render_template, redirect, request, make_response
app = Flask(__name__)

@app.route('/sellerindex', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    if request.method == 'POST':
        sellerid = 123
        itemid = 456
        #itemid = companydb.fetchitemid(request.form['category'], request.form['item'])
        companydb.insertproduct(sellerid, itemid, request.form['quantity'], request.form['unit'])
        return ("successfully added product")
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
        sellerid = 123
        #orderlist = fetchorders(sellerid)
        orderlist = [('123','525','7.2','litre'), ('123','100','2.2','kg')]
        return render_template('orders.html', ordlist=orderlist)

if __name__== '__main__':
    app.run()
