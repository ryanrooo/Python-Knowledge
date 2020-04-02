#Series and Dataframes in pandas



import pandas as pd
import xlwt as xl

#2 Find any csv or tab delimited DataSet online.
table = pd.read_csv("C:/Users/ryann/Documents/Data-Cleaning-Practical-Examples-master/raw_data_unmodified.csv", sep="," )


y = table
name_y = y['movie_title']
bad = ("?ÿ")

#3 Format the dataframe correctly and then print the 1st 5 rows of the dataset
for i in name_y:
    if i.endswith(bad):
        new = (i[:-len(bad)])
        y['movie_title'] = y['movie_title'].replace(i, new)
print (table)


#4 Print each series by themselves
header = table.head()
print (header)

first = table
first_column = first["movie_title"]
print (first_column)


second = table
second_column = second["num_critic_for_reviews"]
print(second_column)

third = table
third_column = third["duration"]
print(third_column)

fourth = table
fourth_column = fourth["DIRECTOR_facebook_likes"]
print(fourth_column)

fifth = table
fifth_column = fifth["budget"]
print(first_column)

sixth = table
sixth_column = sixth["title_year"]
print(sixth_column)

#5 Create a new column combining 2 of the existing columns
new = table
new["movie_review"] = new["movie_title"] + "-" + str(new["num_critic_for_reviews"])
print(new)