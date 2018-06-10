import sqlite3
DATABASE = 'sellerdb.db'

def moveorder(orderid):
    con2 = sqlite3.connect(DATABASE)
    cur2 = con2.cursor()
    cur2.execute("select * from orders where orderid=?",(orderid,))
    datas=cur2.fetchall()
    cur2.close()
    cur5.execute("INSERT INTO acceptorders (orderid,buyerid, sellerid, itemid, qty) values (?,?,?,?,?)", (datas[0],datas[1],datas[2],datas[3],datas[4]))
    cur5.commit
    cur5.close()
    con3 = sqlite3.connect(DATABASE)
    cur3 = con3.cursor()
    cur3.execute("delete from orders where orderid=?",(orderid,))
    con3.commit
    con3.close()

def deleteorder(orderid):
    con4 = sqlite3.connect(DATABASE)
    cur4 = con4.cursor()
    cur4.execute("delete from orders where orders.orderid=orderid")
    con4.commit
    con4.close()

