import Student
import unittest
class  teststudent(unittest.TestCase):
    def test_email(self):
        self.assertEqual(Student.email("shaik"),"shaik")

if __name__=="__main__":
    unittest.main()