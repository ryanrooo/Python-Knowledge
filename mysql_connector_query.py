#Working with databases


import mysql.connector

from tabulate import tabulate

#2
db = mysql.connector.connect(user = 'root', passwd = 'Adm1n__$$', host = '127.0.0.1', database = 'AdventureWorks')
print (db)

mycursor = db.cursor()
mycursor.execute("Show tables")
print (mycursor.fetchall())

#3
tscardtype = db.cursor()
tscardtype.execute( "Select Cardtype, SUM(salesorderheader.TotalDue) AS TotalSales \n "
                    "from salesorderheader \n"
                    "inner join creditcard \n "
                    "on creditcard.creditcardID = salesorderheader.creditcardID \n"
                    "group by Cardtype;" )

tsrcardtype = (tscardtype.fetchall())
print(tabulate(tsrcardtype, headers=['Cardtype', 'TotalDue'], tablefmt='psql'))


#4
tsproduct = db.cursor()
tsproduct.execute(  "select round(sum(salesorderdetail.LineTotal), 2), productcategory.name \n"
                    "from salesorderdetail \n"
                    "inner join product \n"
                    "on product.ProductID = salesorderdetail.ProductID \n"
                    "inner join productsubcategory \n"
                    "on product.ProductSubcategoryID = productsubcategory.ProductSubcategoryID \n"
                    "inner join productcategory \n"
                    "on productcategory.productcategoryID = productsubcategory.productcategoryID \n"
                    "group by productcategory.name;")

tsrproducts = (tsproduct.fetchall())
print(tabulate(tsrproducts, headers=['TotalDue', 'Products'], tablefmt='psql'))


#5
tsrdate = db.cursor()
tsrdate.execute("Select shipdate, round(totaldue, 2) \n"
               "from salesorderheader \n"
               "group by shipdate;")

results =  (tsrdate.fetchall())
print(tabulate(results, headers=['shipdate', 'TotalDue'], tablefmt='psql'))


#6

tsrterrid = db.cursor()
tsrterrid.execute(  "select sum(salesorderheader.TotalDue) as total, salesterritory.Group \n"  
                    "from salesorderheader \n"
                    "inner join salesterritory \n"
                    "on salesorderheader.TerritoryID = salesterritory.TerritoryID \n"
                    "group by salesterritory.Group")

tsrterrid = (tsrterrid.fetchall())
print(tabulate(tsrterrid, headers=['TotalSales', "TerritoryGroup"], tablefmt="psql"))


#7
tsrshipmethod = db.cursor()
tsrshipmethod.execute(  "select sum(salesorderheader.Totaldue) as total, shipmethod.name \n"
                        "from salesorderheader \n"
                        "inner join shipmethod \n"
                        "on shipmethod.shipmethodid = salesorderheader.shipmethodid \n"
                        "group by shipmethod.name")

tsrshipmethod = (tsrshipmethod.fetchall())
print(tabulate(tsrshipmethod, headers=['TotalSales', "TerritoryGroup"], tablefmt="psql"))


#8
tsproductsub = db.cursor()
tsproductsub.execute(   "select round(sum(salesorderdetail.LineTotal), 2), productsubcategory.name \n"
                        "from salesorderdetail \n"
                        "inner join product \n"
                        "on product.ProductID = salesorderdetail.ProductID \n"
                        "inner join productsubcategory \n"
                        "on product.ProductSubcategoryID = productsubcategory.ProductSubcategoryID \n"
                        "inner join productcategory \n"
                        "on productcategory.productcategoryID = productsubcategory.productcategoryID \n"
                        "group by productsubcategory.name;")

tsrproductsub = (tsproductsub.fetchall())
print(tabulate(tsrproductsub, headers=['TotalDue', 'Products'], tablefmt='psql'))