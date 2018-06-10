import sqlite3
DATABASE = 'companydb.db'

def insertproduct(sellerid, itemid, qty, unit):
	con1 = sqlite3.connect(DATABASE)
	cur1 = con1.cursor()
	cur1.execute("INSERT INTO availproducts (sellerid, itemid, qty, unit) values (?,?,?,?)", (sellerid, itemid, qty, unit))
	con1.commit()
	con1.close()


def fetchitemid(category,item):
	con2 = sqlite3.connect(DATABASE)
	cur2 = con2.cursor()
	cur2.execute("SELECT itemid from items where items.category=category and items.item=item")	
	data=cur2.fetchall()
	con2.close()

def fetchproducts(sellerid):
	con3 = sqlite3.connect(DATABASE)
	cur3 = con3.cursor()
	cur3.execute("SELECT * from availproducts where sellerid=?",(sellerid,))
	datapro=cur3.fetchall()
	print(datapro)
	con3.close()
	return datapro

def fetchorders(sellerid):
    con1 = sqlite3.connect(DATABASE)
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM orders where sellerid=?",(sellerid,))
    datapro=cur1.fetchall()
    print (datapro)
    con1.close()
    return datapro
