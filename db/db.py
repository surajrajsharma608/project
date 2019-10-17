import mysql.connector

con = mysql.connector.connect\
        (
         host = 'localhost',
         user = 'root',
         passwd = '',
         database = 'resturant'
        )
cur = con.cursor()
def user_login(tup):
    try:
        cur.execute("SELECT * FROM login WHERE email = %s AND password = %s",tup)
        return (cur.fetchone())
    except:
        return False
def insert_register_data(tup):
    cur.execute("INSERT INTO login (username,email,password) VALUES(%s,%s,%s)",tup)
    con.commit()
    return True

#for the staff management
def insert_staff(tup):
    cur.execute("INSERT INTO staffs (name,address,phone,gender,salary,position) VALUES(%s,%s,%s,%s,%s,%s)",tup)
    con.commit()
    return True
def view_table():
    cur.execute("SELECT * FROM staffs")
    return cur.fetchall()

#for the products management
def insert_products(tup):
    cur.execute("INSERT INTO product (itemname,price,type) VALUES(%s,%s,%s)",tup)
    con.commit()
    return True
def view_products():
    cur.execute("SELECT * FROM product")
    return cur.fetchall()
#for insert records on option menu
def insert_on_qty_optionmenu():
    cur.execute("SELECT itemname FROM product")
    return cur.fetchall()
def insert_on_type_menu():
    cur.execute("SELECT type FROM product")
    return cur.fetchall()
