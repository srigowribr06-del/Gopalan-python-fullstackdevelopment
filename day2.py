#######FOR LOOP######
#for i in range(10):
#    print("Python")

######WHILE LOOP########
#i=1
#while i<=5:
#   print("hello world")
#    i+=1

###########FUNC WITHOUT PARAMETER#########
#def greet():
#    print("hello students")
#    print("welcome to python")
#greet()

#########FUNC WITH PARAMETER#######
#def add(a,b,c):
#    result=a+b+c
#    print(result)
#add(10,20,30)
#add(10,30,10)

###########LIST##########
#students=["gowri","shree","hajira","hema"]
#students.append("niki")
#students.remove("hema")
#students.insert(2,"hema")
#print(students)

########TUPLE###########
#student_details=("nibba",23,67.7,True)
#print(student_details[1])

#######DICTIONARY##########
#student={
#    "name":"nibbi",
#    "usn":"1gd24cs148",
#    "sem":5,
#    "dept":"CSE"
#}
#student["course"]=("python programming")
#student["usn"]="1gd24cs148"
#print(student["name"])
#print(student["usn"])
#print(student["sem"])
#print(student["dept"])
#print(student["course"])

#######CLASS & OBJECTS#######
#class students:
#    def display(self):
#        print("hello")
#        print("python")
#s1=student()
#s1.display()

##########CONSTRUCTOR##########
# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Marks:",self.marks)
# s1=student("nibbi",23,67.5)
# s2=student("nibba",24,45.4)
# s1.display()
# s2.display()

##########ENCAPSULATIOM##########
# class student:
#     def __init__(self):
#         self.__marks=0

#     def set_marks(self,marks):
#         self.__marks=marks

#     def show_marks(self):
#         print("student marks:",self.__marks)

#         s1=student()
#         s1.set_marks(85.5)
#         s1.show_marks()

############INHERITANCE##########
#class father:
#    def house(self):
#        print("father has a house")
#class son(father):
#    def car(self):
#        print("son has a car")

# s=son()
# s.house()
# s.car()

###########MULTIPLE INHERITANCE##########
# class grandfather:
#     def land(self):
#         print("grandfather has a land")

# class father(grandfather):
#     def house(self):
#         print("father has a house")

# class son(father):
#     def car(self):
#         print("son has a car")

# s=son()
# s.land()
# s.house()
# s.car()

###########HIERARCHICAL INHERITANCE##########
# class father:
#     def land(self):
#         print("father has a land")

# class son(father):
#     def house(self):
#         print("son has a house")

# class daughter(father):
#     def car(self):
#         print("daughter has a car")

# s=son()
# d=daughter()
# s.land()
# s.house()
# d.car()

###########POLYMORPHISM##########
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# animal=[Dog(),Cat(),Animal()]
# for animal in animal:
#     animal.sound()

##############ABSTRACTION##########
from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(payment):
    def pay(self,amount):
        print("paid using UPI:",amount)

class Card(payment):
    def pay(self,amount):
        print("paid using Card:",amount)

p1=UPI()
p2=Card()
p1.pay(1000)
p2.pay(2000)
        
