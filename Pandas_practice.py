'''
#Pandas can clean messy data sets, and make them readable and relevant.
#Relevant data is very important in data science.
import pandas
mydata_set   = {
    'cars':['BMW','Inova','Maruti'],'passing':[3,6,9]
    }
val = pandas.DataFrame(mydata_set)
print(val)'''

'''
#Pandas is usually imported under the pd alias.
#alias: In Python alias are an alternate name for referring to the same thing.
#Create an alias with the as keyword while importing:
import pandas as pd
mydata_set   = {
    'cars':['BMW','Inova','Maruti'],'passing':[3,6,9]
    }
val = pd.DataFrame(mydata_set)
print(val)'''

'''
# TO check pandas version
import pandas as pd
print(pd.__version__)'''

'''
#What is a Series?
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.
import pandas as pd
a = [4,5,6,"Apple"]
myval = pd.Series(a)
print(myval)
print(myval[3])'''

'''
#Create Labels
#With the index argument, you can name your own labels.
import pandas as pd
a = [7,8,9]
myval = pd.Series(a,index=["x","y","z"])
print(myval["y"])
print(myval)'''

'''
#Key/Value Objects as Series
#You can also use a key/value object, like a dictionary, when creating a Series.
import pandas as pd
calories = {"day1":200,"day2":300,"day3":400}
myval = pd.Series(calories)
print(myval[2])
print(myval)'''

'''
#DataFrames
#Data sets in Pandas are usually multi-dimensional/2 Dimensional tables, called DataFrames.
#Series is like a column, a DataFrame is the whole table.
import pandas as pd
data = {"calories" : [100,200,300],
        "duration":[2,3,4]}
variable = pd.DataFrame(data)
print(variable)'''

'''
#Locate Row
#As you can see from the result above, the DataFrame is like a table with rows and columns.
#Pandas use the loc attribute to return one or more specified row(s)
#Note: This example returns a Pandas Series.
import pandas as pd
data = {"calories" : [100,200,300,400,500,600],
        "duration":[2,3,4,5,6,7]}
variable = pd.DataFrame(data)
print(variable.loc[0])
print(variable.loc[[0,4,5]])'''

'''
#Named Indexes
#With the index argument, you can name your own indexes.
import pandas as pd
data = {"Name":['usman','afroz','ateeq'],
        "id":[101,102,103]}
result = pd.DataFrame(data,index=["day1","day2","day3"])
print(result)
print(result.loc[["day2"]])'''

'''
#Read CSV Files
#A simple way to store big data sets is to use CSV files (comma separated files).
#CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
#In our examples we will be using a CSV file called 'data.csv'.
import pandas as pd
df = pd.read_csv('C:/Users/user744/PycharmProjects/pythonProject1/data.csv.txt')
print(df)
#use to_string() to print the entire DataFrame.
#print(df.to_string())
#The number of rows returned is defined in Pandas option settings.
#You can check your system's maximum rows with the pd.options.display.max_rows statement.
print(pd.options.display.max_rows)'''

'''
#Increase the maximum number of rows to display the entire DataFrame:
import pandas as pd
pd.options.display.max_rows=200
df = pd.read_csv('C:/Users/user744/PycharmProjects/pythonProject1/data.csv.txt')
print(df)'''
'''
#Viewing the Data
#One of the most used method for getting a quick overview of the DataFrame, is the head() method.
#The head() method returns the headers and a specified number of rows, starting from the top.
import pandas as pd
df = pd.read_csv('C:/Users/user744/PycharmProjects/pythonProject1/data.csv.txt')
print(df.head(10))
#There is also a tail() method for viewing the last rows of the DataFrame.
#The tail() method returns the headers and a specified number of rows, starting from the bottom.
import pandas as pd
df = pd.read_csv('C:/Users/user744/PycharmProjects/pythonProject1/data.csv.txt')
print(df.tail(3))
#The DataFrames object has a method called info(), that gives you more information about the data set.
print(df.info())'''









