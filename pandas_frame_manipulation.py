#Essential Panda Operations


import pandas as pd

table = pd.read_csv("C:/Users/Ryann/Documents/Consumer_Complaints.csv")
print (table)
print(table.shape)


#4 Delete the following columns and then display the 1st 5 rows in the new dataset
head = table.head()

print (head)

#5 Delete the following columns and then display the 1st 5 rows in the new dataset

drop = table.drop(["Consumer complaint narrative", "Company public response", "Consumer consent provided?", "Consumer disputed?", "Complaint ID", "Tags", "Issue"], axis=1)
print (drop.shape)


#6 How many rows and columns are in the dataset.


print (drop.shape)


#7 Delete rows 0 – 1000.  (We did not cover this in the class.  You will need to use the Range function.  Go look at Script3.py for help)

new = table.drop(table.index[1:1001])
print (new)


#8 How many rows and columns are in the dataset.

print (new.shape)

#9 Sort the dataframe by Date Received descending – Print Dataframe

sort = table["Date received"].sort_values(ascending=False)
print (sort)

#10 Find the number of disputes by Company

cdispute = table.groupby('Company').Product.count()
print (cdispute)

#11 Find the number of disputes by State

sdispute = table.groupby('State').Product.count()
print (sdispute)

#12 Find the number of disputes by DateReceived Year, Month descending

table["Date received"] = pd.to_datetime(table["Date received"])

print (table.dtypes)

ymdispute = table.groupby([(table["Date received"].dt.year),(table["Date received"].dt.month)]).Product.count().sort_values(ascending=False)

print (ymdispute)