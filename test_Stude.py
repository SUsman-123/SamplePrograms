import unittest
from stu import Student
ob=Student("shaik","usman",34)
class test_student(unittest.TestCase):
    def test_email(self):
        self.assertEqual(ob.email,"shaik.usman@gmail.com")
    def test_fullname(self):
        ob=Student("shaik","usman",90)        self.assertEqual(ob.fullname,"shaikusman")
    def test_apply_bonus(self):
        ob=Student("Shaik","Usman",60)
        self.assertEqual(ob.marks,60)
        ob.apply_bonus()
        self.assertEqual(ob.marks,90)
    def test_dum(self):
        ob=Student("shaik","usman",50)
        ob.dum("muzz")
        self.assertEqual(ob.somevalue,"shaik.usman@gmail.comshaikusmanmuzz")
        #self.assertEqual(ob.somevalue,"shaik.usman@gmail.comshaik.usman")
if __name__=="__main__":
    unittest.main()