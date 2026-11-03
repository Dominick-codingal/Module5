class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
         return self.a < other.a
    def __eq__(self, other):
        return self.a == other.a

val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: ")) 

#Creating objects
ob1 = A(val1)  
ob2 = A(val2)

print(f"Passed Value: {ob1.a} {ob2.a}")

if ob1 < ob2:
    print(f"{ob1.a} is less than {ob2.a}")
else:
    print(f"{ob2.a} is less than or equal to {ob1.a}")
    
val3 = int(input("\nEnter third value: "))
val4 = int(input("Enter fourth value: "))     

ob3 = A(val3)  
ob4 = A(val4)

print(f"Passed Value: {ob3.a} {ob4.a}")

if ob3 == ob4:
    print(f"{ob3.a} is equall to {ob4.a}")
else:
    print(f"{ob3.a} is not equal to {ob4.a}")
