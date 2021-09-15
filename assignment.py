
import random
from error_assignment import DeleteNo, RandomGenerator

class XSet:
    def __init__(self):
        self.arr = []
        self.hash_map = {}

    #to insert the element from data set
    def insert_method(self, no):
        if no in self.hash_map:
            return
        length_of_list = len(self.arr)
        self.arr.append(no)
        self.hash_map[no]=length_of_list


    #to remove the element from dataset
    def remove_method(self,no):
        index = self.hash_map.get(no, None)
        if index == None :
            raise DeleteNo()
        
        
        del self.hash_map[no]
        #deleted_element = self.arr[index]
        length_of_list = len(self.arr)
        last_element = self.arr[length_of_list-1]
        self.arr[index], self.arr[length_of_list-1] = self.arr[length_of_list-1],self.arr[index]
        del self.arr[-1]
        self.hash_map[last_element] = index


    #to get the random number from dataset
    def getRandomNumber(self):

        if len(self.arr) == 0:
            raise RandomGenerator()

        index = random.randrange(0, len(self.arr))
        return self.arr[index] 

    

if __name__=="__main__":
    ds = XSet()
    
        
    ds.insert_method(10)
    ds.insert_method(20)
    print(ds.getRandomNumber())
    print(ds.arr)
    ds.insert_method(30)
    ds.insert_method(40)
    print(ds.getRandomNumber())
    print(ds.arr)
    ds.insert_method(50)
    print(ds.getRandomNumber())
    print(ds.arr)
    print(ds.getRandomNumber())
    print(ds.arr)
    ds.remove_method(10)
    ds.remove_method(40)
    ds.remove_method(30)
    ds.remove_method(50)
    print(ds.arr)
    
    
