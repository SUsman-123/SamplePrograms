import pyodbc

server = 'HCL-02-NEW-06\SQLEXPRESS'
database = 'FileSearchResult'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class employee:
    Projects=["PYTHON","JAVA","C"]
    def Project(self):
        values='''SELECT PROJECT FROM EMPLOYEE_DETAILS'''
        try:
            for i in self.Projects:
                if i in values:
                    obj.Insert_DataInto_DB()
                    break
                else:
                    print("Please select your project from the list")
                break
        except:
            print("no")

    def Insert_DataInto_DB(self,name,salary,project):
        try:
            for i in self.Projects:
                if i in obj.Insert_DataInto_DB():
                    Query = '''  INSERT INTO EMPLOYEE_DETAILS (NAME,SALARY,PROJECT)
                                VALUES
                                ('{0}',{1},'{2}')  '''
                    insertQuery = Query.format(name,salary,project)
                    cursor.execute(insertQuery)
                    cnxn.commit()
                    print("EMPLOYEE DETAILS ADDED TO DATABASE")
                else:
                    print("WRONG PROJECT HAS BEEN SELECTED")
        except:
            print("no")

    def add_bonus(self,salary,bonus):
        try:
            if bonus==20:
                bonus1=salary*bonus/100
                Query1 = '''  UPDATE EMPLOYEE_DETAILS SET SALARY={}'''
                insertQuery = Query1.format(salary+bonus1)
                cursor.execute(insertQuery)
                cnxn.commit()
                print("BONUS HAS BEEN ADDED TO YOUR SALARY")
            else:
                print("INKENTHA KAVALI RA NEEKU BONUS")
        except:
            print("nono")

obj=employee()
obj.Insert_DataInto_DB('USMAN',60000,'PYTHO')
obj.Insert_DataInto_DB('SRUTHILAYA',70000,'JAVA')
obj.Insert_DataInto_DB('SRINIVAS',70000,'C')
obj.add_bonus(70000,20)
obj.Project()


















import pyodbc
server = 'HCL-02-NEW-06\SQLEXPRESS'
database = 'FileSearchResults'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Employee_Project1:

    def Create_Employee_Table_in_db(self):
            Query =cursor.execute('''  
                            CREATE TABLE Employee_Details (
                            Name varchar(50),
                            Salary int,
                            Project varchar(50))
                            ''')
            cnxn.commit()
            print("Table created in database")

            def upload_employee_details(self, Name, Salary, Project):
                query = '''  
                                   INSERT INTO Employee_Details (Name, Salary, Project)
                                   VALUES
                                   ('{0}',{1},'{2}')  '''

                insertQuery = query.format(Name, Salary, Project)
                cursor.execute(insertQuery)
                cnxn.commit()
                print("Employee Details uploaded")

