from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def move(self):
        pass
    
 #subclass
class human(Animal):
    def move(self):
        print("I can walk")
        
class Snake(Animal):
    def move(self):
        print("I can slither")        

class Dog(Animal):
    def move(self):
        print("I can bark")        
        
class Lion(Animal):
    def move(self):
        print("I can roar")

animals = [human(), Snake(), Dog(), Lion()]

for animal in animals:
    animal.move()