###         OOPS            ###

##  Abstrction
from abc import ABC,abstractmethod

class maths(ABC):
    def __init__(self,data) -> None:
        pass
        
    @abstractmethod
    def equal(self):
        pass

class calculate(maths):
    def __init__(self, data) -> None:
        super().__init__(data)

    def equal(self):
        print("==")

    def addition(self):
        print("Addition")

p1=calculate("Add")
p1.equal()
p1.addition()

###         ENcapsulation

class password_strength_checker:
    def __init__(self,password) -> None:
        self.__password =password
    
    @property
    def checker(self):
        return self.__password
    
    @checker.setter
    def checker(self,pass_word):
        if pass_word==self.__password:
            print("password Accepted")
        else:
            print("password is wrong")

p1=password_strength_checker("90123847")
user_password=str(input("Enter password :"))
p1.checker= user_password

