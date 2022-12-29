import pyodbc
import time
start=time.perf_counter()
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'HCL-02-NEW-06\SQLEXPRESS'
database = 'FileSearchResults'
username = 'capstone'
password = 'Capstone@123'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
print(cnxn)
cursor = cnxn.cursor()
print(cursor)
cursor.execute('''
                INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                VALUES
                ('E:\shaik\Team1\Team2\Test_1.txt',1,'Test_1')
                ''')
cnxn.commit()
values=cursor.execute('select * from FileSearchResults_table')
for i in values:
    print(i)

finish = time.perf_counter()
print(f'Finish in {finish - start}seconds')