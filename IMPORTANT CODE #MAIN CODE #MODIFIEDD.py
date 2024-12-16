# Add order function with salesid logic
import datetime
import mysql.connector as m
conn=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
if conn.is_connected()==False:
    print("Error In Establishing Databases Connection")
else:
    print("Database Connection Has Been Established Sucessfully")
    cursor=conn.cursor()

def product_management():
    while True:
        print("------------------------------")
        print("1.ADD NEW PRODUCT")
        print("2.LIST PRODUCT")
        print("3.UPDATE PRODUCT")
        print("4.DELETE PRODUCT")
        print("5.BACK TO MAIN MENU(EXIT)")
        print("------------------------------------")
        p=int(input("Enter Your Choice(1-5)"))
        if p==1:
            add_product()
        if p==2:
            search_product()
        if p==3:
            update_product()
        if p==4:
            delete_product()
        if p==5:
            print("BACK TO MAIN MENU")
            print("--------------------------")
            break
        
def add_product():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    sql="INSERT INTO product(pcode,pname,pprice,pqty,cat) values(%s,%s,%s,%s,%s)"
    code=int(input("Enter product code :"))
    search="SELECT count(*) FROM product WHERE pcode=%s;"
    val=(code,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt=x[0]
        if cnt==0:
            name=input("Enter product name:")
            qty=int(input("Enter product quantity:"))
            price=float(input("Enter product unit price:"))
            cat=input("Enter Product category:")
            val=(code,name,price,qty,cat)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            print("\t\t Product already exist")
            
def list_product():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT * from product"
    mycursor.execute(sql)
    print("PRODUCT DETAILS")
    print("code \t name \t\t\t price \t quantity \tcategory")
    for i in mycursor:
        print(i[0],"",i[1],"\t",i[2],"\t",i[3],"",i[4])
        
def update_product():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    code=int(input("Enter the product code :"))
    qty=int(input("Enter the quantity :"))
    sql="UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
    val=(qty,code)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Product details updated")
    
def delete_product():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    code=int(input("Enter the product code :"))
    sql="DELETE FROM product WHERE pcode = %s;"
    val=(code,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount," record(s) deleted")
    
def search_product():
    while True :
        print("\t\t\t 1. List all product")
        print("\t\t\t 2. List product code wise")
        print("\t\t\t 3. List product categoty wise")
        print("\t\t\t 4. Back (Main Menu)")
        s=int (input("\t\tEnter Your Choice :"))
        if s==1 :
            list_product()
        if s==2 :
            code=int(input(" Enter product code :"))
            list_prcode(code)
        if s==3 :
            cat=input("Enter category :")
            list_prcat(cat)
        if s== 4 :
            break
        
def list_prcode(code):
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT * from product WHERE pcode=%s"
    val=(code,)
    mycursor.execute(sql,val)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*90)
    print("\t\t code \t name \t\t\t price \t quantity \t category")
    print("\t\t","-"*90)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t",i[4])
        print("\t\t","-"*90)
        
def list_prcat(cat):
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    print (cat)
    sql="SELECT * from product WHERE cat =%s"
    val=(cat,)
    mycursor.execute(sql,val)
    clrscr()
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*90)
    print("\t\t code \t name \t\t\t price \t quantity \t category")
    print("\t\t","-"*90)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t",i[4])
        print("\t\t","-"*90)
        
def clrscr():
    print("\n"*5)
    
def list_order():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT*from orders"
    mycursor.execute(sql)
    print("ORDER DETAILS")
    for i in mycursor:
        print("orderid Date Productcode price quantity Supplier Category")
        print(i[0],"\t",i[1],"",i[2],"",i[3],"",i[4],"",i[5],"",i[6])
        
        
def user_management():
    while True:
        print("----------------")
        print("1.ADD UDER")
        print("2.LIST USER")
        print("3.BACK-TO-MAIN-MENU(EXIT)")
        print("----------------")
        p=int(input("Enter Your Choice(1-3)"))
        if p==1:
            add_user()
        if p==2:
            list_user()
        if p==3:
            print("BACK TO MAIN MENU")
            break

def add_user():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    uid=input("Enter emaid id :")
    name=input(" Enter Name :")
    paswd=input("Enter Password :")
    sql="INSERT INTO users values (%s,%s,%s);"
    val=(uid,name,paswd)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, " user created")

def list_user():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT uid,name from users"
    mycursor.execute(sql)
    print("USER DETAILS")
    print("","-"*27)
    print("\t\t UID \t\t\t name ")
    print("\t\t","-"*27)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1])
        print("\t\tx","-"*27)

def sales_management():
    while True:
        print("----------------")
        print("1.SALES ITEM")
        print("2. LIST ITEMS")
        print("3.BACK-TO-MAIN-MENU(EXIT)")
        print("----------------")
        p=int(input("Enter Your Choice(1-3)"))
        if p==1:
            sale_product()
        if p==2:
            list_sale()
        if p==3:
            print("BACK TO MAIN MENU")
            break
        
def sale_product():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    pcode = input("Enter product code: ")
    # Check if the product exists in the product table
    sql = "SELECT count(*) FROM product WHERE pcode=%s;"
    val = (pcode,)
    mycursor.execute(sql, val)
    # Fetch the count of matching products
    cnt = mycursor.fetchone()[0]
    if cnt != 0:
        sql = "SELECT * FROM product WHERE pcode=%s;"
        mycursor.execute(sql, val)
        product = mycursor.fetchone()
        if product:
            print(product)
            price = int(product[2]) # Assuming price is the 3rd column
            pqty = int(product[3]) # Assuming quantity is the 4th column
            qty = int(input("Enter number of quantity: "))
            if qty <= pqty:
                total = qty * price
                print(f"Collect Rs. {total}")
                sql1 = "SELECT MAX(salesid) FROM sales;"
                mycursor.execute(sql1)
                c = mycursor.fetchone()
                last = c[0] if c[0] is not None else 0
                salesid = int(last) + 1
                sql = "INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s);"
                val = (salesid, datetime.date.today(), pcode, price, qty,total)
                mycursor.execute(sql, val)
                sql = "UPDATE product SET pqty = pqty - %s WHERE pcode = %s;"
                val = (qty, pcode)
                mycursor.execute(sql, val)
                mydb.commit()
            else:
                print("Quantity not available.")
        else:
            print("Product details not found.")
    else:
        print("Product is not available.")


def list_sale():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT * FROM sales"
    mycursor.execute(sql)
    print(" \t\t\t\tSALES DETAILS")
    print("-"*110)
    print("Sales id \t Date \t\t ProductCode \t Price \t Quantity \t\tTotal")
    print("-"*110)
    for x in mycursor:
        print(x[0],"\t",x[1],"\t",x[2],"\t\t",x[3],"\t",x[4],"\t\t",x[5])
        print("-"*110)

def db_management( ):
    while True :
        print("\t\t\t 1. Database creation")
        print("\t\t\t 2. List Database")
        print("\t\t\t 3. Back (Main Menu)")
        p=int (input("\t\tEnter Your Choice :"))
        if p==1 :
            create_database()
        if p==2:
            list_database()
        if p== 3 :
            break
        
def create_database():
    print(" Creating PRODUCT table")
    sql1 = "CREATE TABLE if not exists product (pcode char(30) PRIMARY KEY,pname varchar(30),pprice float,pqty int,cat varchar(20));"
    cursor.execute(sql1)
    print("Product Table Created Sucesfully")
    print()
    print(" Creating ORDER table")
    print()
    cursor.execute("USE STOCK;")
    sql="CREATE TABLE if not exists orders (orderid INT AUTO_INCREMENT PRIMARY KEY,orderdate DATE NOT NULL,pcode INT NOT NULL,pprice FLOAT NOT NULL,pqty INT NOT NULL,supplier VARCHAR(255) NOT NULL,pcat VARCHAR(255) NOT NULL);"
    cursor.execute(sql)
    print("Order Table Created Sucesfully")
    print()
    print(" Creating SALES table")
    cursor.execute("USE STOCK;")
    sql="CREATE TABLE if not exists sales (salesid varchar(40) PRIMARY KEY,salesdate varchar(40),pcode char(30) references product(pcode),pprice float(8,2),pqty int(4),Total double(8,2));"
    cursor.execute(sql)
    print("Sales Table Created Sucesfully")
    print()
    print(" Creating USERS table")
    cursor.execute("USE STOCK;")
    sql="CREATE TABLE  if not exists users (uid VARCHAR(20) PRIMARY KEY,name VARCHAR(255) NOT NULL,paswd VARCHAR(255) NOT NULL);"
    cursor.execute(sql)
    print("Users Table Created Sucesfully")
    print()
    
def list_database():
    mydb=m.connect(host="localhost",user="root",passwd="moksh24",database="stock")
    mycursor=mydb.cursor()
    sql="show tables;"
    mycursor.execute(sql)
    for i in mycursor:
        print(i)

while True:
    print("STOCK MANAGEMENT")
    print("----------------")
    print("1.PRODUCT MANAGEMENT")
    print("2.SALES MANAGEMENT")
    print("3.USER MANAGEMENT")
    print("4.DATABASE SETUP")
    print("5.Exit")
    print("----------------")
    x=int(input("Enter Your Choice(1-6)"))
    print("-----------------------")
    if x==1:
        product_management()
    if x==2:
        sales_management()
    if x==3:
        user_management()
    if x==4:
        db_management()
    if x==5:
        break
