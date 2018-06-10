import sqlite3 as sql

def insertUser(email,username,password,phone,district):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email,username,password,phone,district) VALUES (?,?,?,?,?)", (email,username,password,phone,district))
    con.commit()
    con.close()

def checkUser(username,password):
	con=sql.connect("database.db")
	cur=con.cursor()
	cur.execute("SELECT password from users where username=?",(username,))
	cred=cur.fetchone()
	con.close()
	if cred is not None:
		if password==cred[0]:
			return 1
	return 0


def fetchItemId(product):
	con=sql.connect("database.db")
	cur=con.cursor()
	cur.execute("SELECT itemid from items where item=?",(product,))
	prod=cur.fetchone()
	con.close()
	return prod


def fetchinfo(user_id,item_id):
	con=sql.connect("database.db")
	cur=con.cursor()
	cur.execute("SELECT itemid from availproducts where sellerid=?",(user_id,))
	dist=cur.fetchall()
	con.close()
	return dist



def fetchUserId(dist):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT id FROM users where district=?",(dist,))
	users = cur.fetchall()
	con.close()
	return users

# def findUserName(userId):
# 	con = sql.connect("database.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT username FROM users where id=?",(userId,))
# 	users = cur.fetchone()
# 	con.close()
# 	return users
