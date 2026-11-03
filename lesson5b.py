from abc import ABC, abstractmethod

class ABSClass(ABC):
    
    #normal method
    def display(self, x):
        print("passed value: ", x)
        
   #Abstract method
    @abstractmethod
    def task(self):
        print("we are inside ABSClass task")
#Subclass to  implement the abstract
class TestClass(ABSClass):
    def task(self):
        print("We are inside TestClass task")

obj = TestClass()        
obj.task()
obj.display(100)
    
    