import unittest
import UploadFiles
import filelocation
import pyodbc

server = 'HCL-02-NEW-06\SQLEXPRESS'
database = 'FileSearchResults'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


class test_capstone(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_upload_file_results_todb(self):
        uploadObj = UploadFiles.UploadFilesToDB()
        fileObj = filelocation.FindFileLocation()
        uploadObj.upload_file_results_todb("Test_1.txt",
                                           "E:\shaik\Team1\Team2\Team3\Team4\Team5\Team6\Team7\Team8\Team9\Team10\\Test_1.txt",
                                           0)
        # uploadObj.upload_file_results_todb("test.txt","C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\test.txt", 0)

        values_1 = cursor.execute(
            ''' select * from FileSearchResults_table where NameOfFile = 'Test_1.txt' ''')

        # values_2 = cursor.execute(''' select * from FileSearchResults_table where NameOfFile = 'test.txt' ''')
        for fileInfo in values_1:
            self.assertEqual(fileInfo.NameOfFile, "Test_1.txt")
            self.assertEqual(fileInfo.File_Location,
                             "E:\shaik\Team1\Team2\Team3\Team4\Team5\Team6\Team7\Team8\Team9\Team10\\Test_1.txt")
        for fileInfo1 in values_2:
            self.assertEqual(fileInfo1.NameOfFile, "test.txt")
            self.assertEqual(fileInfo1.File_Location, "C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata")

if _name_ == "_main_":
    unittest.main(verbosity=2)