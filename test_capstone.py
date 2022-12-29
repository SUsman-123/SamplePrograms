import unittest
import UploadFiles
#import Vyshnavi
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
        #newfileob= Vyshnavi.FindFileLocation()
        uploadObj.upload_file_results_todb("yahoo.txt",
                                           "E:\yahoo.txt",0)
        # uploadObj.upload_file_results_todb("test.txt","C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\test.txt", 0)

        values_1 = cursor.execute(
            ''' select * from FileSearchResults_table where NameOfFile = 'yahoo.txt' ''')

        # values_2 = cursor.execute(''' select * from FileSearchResults_ta
        # le where NameOfFile = 'test.txt' ''')
        for fileInfo in values_1:
            self.assertEqual(fileInfo.NameOfFile, "yahoo.txt")
            self.assertEqual(fileInfo.File_Location, "E:\yahoo.txt")

    def test_search_in_db_for_file(self):
        searchObj = UploadFiles.UploadFilesToDB()
        searchObj.search_in_db_for_file('yahoo.txt')
        value_1 = cursor.execute(''' select * from FileSearchResults_table where NameOfFile = 'yahoo.txt' ''')
        for fileInfo in value_1:
            self.assertEqual(fileInfo.NameOfFile, 'yahoo.txt')

if __name__ == "_main_":
    unittest.main()