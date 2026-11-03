class myClass:
    __privateVar = 35

    def __privMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private variable value:", myClass.__privateVar)
        self.__privMeth()


Boo = myClass()
Boo.hello()
Boo.__privMeth
