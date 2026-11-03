class Parrot:
    species = "bird" 
    
    def __init__(self, name, age):   
        self.name = name
        self.age = age

blu = Parrot("Blu", 9)    
woh = Parrot("Woh", 12)

print("Blu is a {}".format(blu.species))
print("Woh is a {}".format(woh.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woh.name, woh.age))
