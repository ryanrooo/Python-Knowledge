import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import sqlalchemy
import xlwt as xl
import xlrd

statehead = ["ID", "State", "AB", "Country", "Type", "Region", "Division"]
balmarthead = ["RowID", "Priority", "Discount", "UnitPrice", "Shipping Cost", "Customer ID","Customer Name","Ship Mode", "Customer Segment", "Category", "Sub-Category", "Package", "Product", "Product Base Margin", "Country", "Region", "State", "City", "Zip", "Order Date", "Ship Date", "Profit", "Quantity", "Sales", "Order ID" ]
balmart = pd.read_excel("C:/Users/Ryann/Documents/Balmart_Store.xlsx", header=None, names=balmarthead)
state = pd.read_csv("C:/Users/Ryann/Documents/state_table.csv", header=None, names=statehead, encoding='cp1252')
date = pd.read_excel("C:/Users/Ryann/Documents/Date_dim.xlsx")

print (balmart)
print (state)
print (date)

engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:Adm1n__$$@127.0.0.1/balmart")
connection = engine.connect()

balmart.to_sql("balmart", engine, if_exists="replace")
date.to_sql("date", engine, if_exists="replace")
state.to_sql("state", engine, if_exists="replace")