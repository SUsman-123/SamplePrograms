import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=HCL-02-NEW-06\SQLEXPRESS;'
                      'Database=FileSearchResults;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('''
               INSERT INTO FileSearchResults_table(File_Location, SearchCount, NameOfFile)
               VALUES
               ('E:\Usman.txt',1,'Test_1.txt'),
               ('E:\Usman\Usman1\Usman2',2,'Test_1.txt')
                            ''')
conn.commit();
cursor.execute('select * from FileSearchresults_table')



