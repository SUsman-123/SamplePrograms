import pyodbc

server = 'HCL-02-NEW-06\SQLEXPRESS'
database = 'FileSearchResults'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
# This class is used to connect to sql db to upload and retrive file search results
class UploadFilesToDB:
    # This Method  is used to display all the available file search results stored in our db table
    def show_file_search_results_fromdb(self):
        values = cursor.execute('select * from FileSearchResults_table')
        for fileInfo in values:
            print("File Name: {}".format(fileInfo.NameOfFile))
            print("File Location: {}".format(fileInfo.File_Location))

    # This Method is used to uploads file and search results into our db table
    # inputs: It accpets filename (name of newly searched file), filelocation (location of file in our drive) and searchcount
    def upload_file_results_todb(self,fileName, fileLocation, searchCount):
        query = '''  
                    INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                    VALUES
                    ('{0}',{1},'{2}')  '''

        insertQuery = query.format(fileLocation, searchCount, fileName)
        cursor.execute(insertQuery)
        cnxn.commit()
        print("New file search results committed to DB")

    # searches for a file in db
    # Input : Filename (string)
    # output : True or False (Boolean)
    def search_in_db_for_file(self, fileName):
        # select query
        query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        values = cursor.execute(searchQuery)
        print("File search results from DB.")
        flag=1

        for fileInfo in values:
            #print("==========================")
            print("File name: {} - File path: {} ".format(fileInfo.NameOfFile, fileInfo.File_Location))
            flag=0
            #print("File path: {}".format(fileInfo.File_Location))
            #print("==========================")
        if flag == 0:
            self.update_file_searchcount(fileName)
            return True
        else:
            return False
    # Method update_file_searchcount is used to update search count of a file. Searchcount is used to determine most searched files
    def update_file_searchcount(self, fileName):
        try:
            query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
            searchQuery = query.format(fileName)
            values = cursor.execute(searchQuery)
            for fileInfo in values:
                fileSearchCount = fileInfo.SearchCount
                # constructing update query to increase file search count by 1
                fileinfoQuery = '''
                        Update FileSearchResults_table SET SearchCount = {0} WHERE NameOfFile = '{1}'
                        '''
                updateQuery = fileinfoQuery.format((fileSearchCount + 1), fileName)
                cursor.execute(updateQuery)
                cursor.commit()
                print("Updated file search count")

        except:
            pass