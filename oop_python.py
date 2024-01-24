class Student :
    num_of_student = 0
    def __init__(self,name,age=0,courses="none"): 
        self.__name = name
        self.__age = age
        self.courses = courses
        Student.num_of_student += 1 

    def getName(self):
        return self.__name
    def setName(self, newName):
        self.__name = newName

    def getAge(self):
        return self.__age
    def setAge(self, newAge):
        self.__age = newAge

    def describe (self):
        print(f"My Name is : {self.__name} and My age is : {self.__age}" )
    
    def is_old(self,num):
        if self.__age < num:
            print('student is not old')
        else:
            print('student is old')
        
        

student_1 = Student("Outmane",20,['css','js'])
student_2 = Student("karim",21,['html','css'])

print(student_1.getName())

student_1.setName("oukkoua")
student_1.setAge(30)
student_1.describe()

# ---------------------------------------------------------------------------------------

from datetime import date

class Student :

    def __init__(self,name,age=0):
        self.name = name
        self.age = age
    
    def describe (self):
        print(f"My Name is : {self.name} and My age is : {self.age}" )
    
    @classmethod
    def currentAge(cls,name,birthday):
        return cls(name, date.today().year - birthday)


class Pizza:
    def __init__(self, size, ingredients):
        self.size = size
        self.ingredients = ingredients

    @classmethod
    def veg(cls):
        return cls('medium',['olives', 'tomatoes'])

    @classmethod
    def margaritta(cls):
        return cls('small',['sauceTomato', 'mozarella'])

    def __str__(self):
        return f"pizza ingredients ar {self.ingredients} with size {self.size} \n"
        

pizza_1 = Pizza('xl', ['tomatoes', 'olives']) 
pizza_2 = Pizza.veg() 
pizza_3 = Pizza.margaritta() 

print(pizza_1,pizza_2,pizza_3)


#--------------------------------------------------------------------------------------

class Math :

    @staticmethod
    def add(a , b):
        return a + b
    
    @staticmethod
    def substract(a , b):
        return a - b
    
    @staticmethod
    def multiplication(a , b):
        return a * b
    
    @staticmethod
    def division(a , b):
        return a / b
    
    @staticmethod
    def PI():
        return 3.14

n1 = Math.add(6,4)
n2 = Math.substract(6,4)
n3 = Math.multiplication(6,4)
n4 = Math.division(6,4)
print(n1,n2,n3,n4)


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __str__(self) :
        return f"Pizza ingredients are {self.ingredients} \n"

    def area(self):
        return Pizza.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        return r ** 2 * Math.PI()

p1 = Pizza(6,["olives","tomatos"])
print(p1.area())
print(Pizza.circle_area(10))


# ---------------------------------------------------------------


class Dates :
    def __init__(self,date):
        self.__date = date

    def getDate(self):
        return self.__date
    
    @staticmethod
    def toDashDate(date):
        return date.replace("-","/")
    
date1 = Dates("02/12/2003")

date2 = "02-12-2003"
dash_date = Dates.toDashDate(date2)

if (dash_date == date1.getDate()) :
    print ("equal")
else :
    print ("not equal")

# -----------------------------------------------
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def currentAge(cls,name,birthday,extra):
        today = date.today().year
        return cls(name , today - birthday ,extra)

    def afficher(self):
        return f"name is {self.name} and age is {self.age}"

class Man(Person):
    def __init__(self, name, age, barber):
        super().__init__(name, age)
        self.barber = barber

    def afficher(self):
        base_info = super().afficher()
        return base_info + f" and barber is {self.barber} \n"

class Women(Person):  
    def __init__(self, name, age, hair):
        super().__init__(name, age)
        self.hair = hair

    def afficher(self):
        base_info = super().afficher()
        return base_info + f" and hair is {self.hair} \n"


person1 = Person("outmane", 20)
print(person1.afficher())

person2 = Man("karim", 21, "marocaine")
print(person2.afficher())

person3 = Women("hajar", 20, "marocaine", "curly")
print(person3.afficher())

man = Man.currentAge("outmane",2003,"long")
print(man.afficher())

woman = Women.currentAge("hajar",2000,"curly")
print(woman.afficher())


# ---------------------------------------------------
from abc import ABC,abstractclassmethod

class Shape(ABC) :
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.__side=side
    
    def area(self):
        return self.__side ** 2
    
    def perimeter(self):
        return self.__side * 4
    
class Rect(Shape):
    def __init__(self,length,width):
        self.__length=length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return (self.__length + self.__width) * 2
    

square = Square(10)
print(f"square area is {square.area()} and perimeter {square.perimeter()}")

rect = Rect(10,5)
print(f"rect area is {rect.area()} and perimeter {rect.perimeter()}")


# -----------------------------------------------------------------------------------
class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        names = self.name + " and " + other.name
        ages = self.age + other.age
        return f"Names combined are {names} and the sum of ages is {ages}"

    def __lt__(self, other):
        return self.age < other.age

    def afficher(self):
        return f"My name is {self.name} and I am {self.age}"

man1 = Man("outmane", 20)     
man2 = Man("ali", 30)
print(man1 + man2)

print(man1 < man2)

