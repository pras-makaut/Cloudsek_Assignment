
import unittest 
from assignment import XSet
from error_assignment import DeleteNo, RandomGenerator

class TestAssignment(unittest.TestCase):
    # @classmethod 
    # def setUpClass(cls):
    #     print('super class')
    
    # @classmethod
    # def tearDownClass(cls):
    #     print("terdown class")

    def setUp(self) :
        print('setup')
        self.ds = XSet()
        self.ds.insert_method(10)
        self.ds.insert_method(20)
        self.ds.insert_method(30)
        self.ds.insert_method(40)
    def tearDown(self) :
        print('tear_down')

    def test_randomgenerator(self):
        print('test_randongenerator')
        generated_random_number = self.ds.getRandomNumber()
        self.assertIn(generated_random_number, self.ds.arr)
        self.ds.remove_method(10)
        generated_random_number = self.ds.getRandomNumber()
        self.assertIn(generated_random_number, self.ds.arr)
        self.ds.remove_method(20)
        generated_random_number = self.ds.getRandomNumber()
        self.assertIn(generated_random_number, self.ds.arr)
        self.ds.remove_method(30)
        generated_random_number = self.ds.getRandomNumber()
        self.assertIn(generated_random_number, self.ds.arr)
        self.ds.remove_method(40)
        self.assertRaises(RandomGenerator, self.ds.getRandomNumber)
        

    def test_deletedItemNotInList(self):
        print("test_deletedItemNotInList")
        deleted_number = 10
        self.ds.remove_method(10)
        self.assertNotIn(deleted_number, self.ds.arr)
        deleted_number = 20
        self.ds.remove_method(20)
        self.assertNotIn(deleted_number, self.ds.arr)
        deleted_number = 30
        self.ds.remove_method(30)
        self.assertNotIn(deleted_number, self.ds.arr)
        deleted_number = 40
        self.ds.remove_method(40)
        self.assertNotIn(deleted_number, self.ds.arr)

        self.assertRaises(DeleteNo, self.ds.remove_method, 50)
    
        


if __name__ ==  "__main__":
    unittest.main()



