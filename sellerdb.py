import sqlite3
DATABASE = 'sellerdb.db'

def fetchorders(sellerid):
    con1 = sqlite3.connect(DATABASE)
	cur1 = con1.cursor()
	cur1.execute("select * from orders where sellerid=orders.sellerid")
    orders=cur1.fetchall()
    print orders
	con1.close()