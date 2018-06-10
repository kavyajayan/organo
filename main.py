from flask import Flask, redirect, url_for, session
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

# app.jinja_env.globals.update(findUserName=dbHandler.findUserName)

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
            return redirect(url_for('buyer'))
        else:
            return render_template('index.html',error=True)
        return render_template('index.html', error=False)
    else:
        return render_template('index.html')

# @app.route('/user', methods=['GET','POST'])
# def buyer():
#
# 		return render_template('buyer.html', username=session['username'], )

@app.route('/buyer', methods=['GET','POST'])
def buyer():
    if request.method == 'POST':
        itemid=dbHandler.fetchItemId(request.form['product'])
        userid=dbHandler.fetchUserId(request.form['dist'])
        #productinfo=dbHandler.fetchinfo(userid,itemid)
        return render_template('productlist.html',itemid=itemid,userid=userid)
    else:
        return render_template('buyer.html')






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


@app.route('/create',methods=['POST','GET'])
def subcreate():
	if request.method=='POST':
		subject=request.form['subject']

		dbHandler.addsubject(subject)
		return redirect(url_for('dash'))
	else:
		return render_template('createsub.html')



@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
