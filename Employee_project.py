import pyodbc
server = 'HCL-02-NEW-06\SQLEXPRESS'
database = 'FileSearchResults'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Employee_Project1:
    def add_bonus(self,salary,bonus):
            bonus1 = salary + bonus
            Query1 = '''  UPDATE EMPLOYEE_DETAILS SET Salary={0} '''
            #insertQuery = Query1.format(bonus1)
            cursor.execute(Query1)
            cnxn.commit()
            print("BONUS HAS BEEN ADDED TO YOUR SALARY")
obj=Employee_Project1()
#obj.upload_employee_details('USMAN','60000','JAVA')
#obj.upload_employee_details('SHRUTI','50000','PYTHON')
#obj.upload_employee_details('GOWTHAM','70000','C')
obj.add_bonus(70000,2)


