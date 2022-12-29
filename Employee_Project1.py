#import Schema_1
import pyodbc
server = 'HCL-02-NEW-06\SQLEXPRESS'
database = 'FileSearchResults'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Existing(Exception):
    pass
class Not_in_Range(Exception):
    pass
class Employee_data:
    Bonus=2
    Projects=['Python','C','Java']
    def __init__(self,Name,Salary,Project,Emp_Id):
        self.Name=Name
        self.Salary=Salary
        self.Project=Project
        self.Emp_Id=Emp_Id
    def insert_values_in_table(self):
        try:
            query = '''  
                            INSERT INTO Employee_Details (Name, Salary, Project,Emp_Id)
                            VALUES
                            ('{0}',{1},'{2}',{3})  '''

            insertQuery = query.format(self.Name, self.Salary, self.Project,self.Emp_Id)
            cursor.execute(insertQuery)
            cnxn.commit()
            print("1 row inserted")
        except:
            print("Primary key not accept the same values")
    def Update_Salary(self,New_Salary,Name):
        try:
            self.New_Salary = New_Salary
            self.Name=Name
            if self.New_Salary != self.Salary:
                fileinfoQuery = '''
                                                Update Employee_Details SET Salary ='{0}' WHERE Name = '{1}'
                                                '''
                updateQuery = fileinfoQuery.format(New_Salary,self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise Existing
        except Existing:
            print("No Change in Salary")
    def Add_Bonus(self,bonus,Name):
        self.bonus=bonus
        self.Name=Name
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise Not_in_Range
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''
                        Update Employee_details SET Salary ='{0}' WHERE Name = '{1}'
                                                                '''
                updateQuery = Query.format(self.Salary, self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
        except Not_in_Range:
            print("Bonus is Not in Range")
    def Change_Project(self,project,Name):
        self.project=project
        self.Name=Name

        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update Employee_details SET Project ='{0}' WHERE Name = '{1}' '''
                updateQuery = Query.format(project, Name)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")
    def Display_details(self):
        query=''' select * from Employee_details WHERE Name='{0}' '''
        query1=query.format(self.Name)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0}  Salary:{1}  Project:{2}".format(details.Name , details.Salary , details.Project))
    def Delete_Employee_table(self):
        Query = ''' delete from Employee_details where Name='Usman'  '''
        cursor.execute(Query)
        cursor.commit()
        print("Employee has been deleted")

obj1=Employee_data('Usman','JAVA',52000,1)
obj1.insert_values_in_table()
obj=Schema_1.employee_schema()
obj.employee_table()
obj1.insert_values_in_table()
obj1.Update_Salary(35000,'Usman')
obj1.Add_Bonus(1,'Usman')
obj1.Change_Project('Java','python')
obj1.Display_details()
obj1.Delete_Employee_table()

