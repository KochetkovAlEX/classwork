import math
import random
import time
from abc import ABC,abstractmethod
# class Stack():
#     __count=0
#     def __init__(self,size):
#         self.size=size
#         self.__list=["" for i in range(size)]
#
#     def show(self):
#         print("[",end=" ")
#         for i in range(self.__count):
#             print(self.__list[i],end=" ")
#         print("]")
#     def push(self,num):
#         if self.__count==self.size:
#             raise IndexError("Элементы в списке закончились")
#         else:
#             self.__list[self.__count]=num
#             self.__count+=1
#
#
#
#     def pop(self):
#             if self.__count==0: raise IndexError("Список пуст")
#             else:
#                 self.__count-=1
#
#     def show_size(self):
#         print(self.__count)
#
#
# if __name__=="__main__":
#     try:
#         lst=Stack(5)
#         for i in range(6):
#             lst.push(random.randint(0,9))
#         lst.show()
#         for i in range(6):
#             lst.pop()
#     except Exception as er:
#         print(er)


class Queue():
	__count = 0
	def __init__(self,size):
		self.size=size
		self.list=["" for i in range(self.size)]

	def show(self):
		for i in range(self.__count):
			print(self.list[i],end=" ")
		print()

	def push(self,num):
		if self.__count==self.size: raise Exception("Вышел за пределы. Plus Ultra")
		else:
			self.list[self.__count]=num
			self.__count+=1

	def pop(self):
		if self.__count==0: raise Exception("Ouch. List empty")
		for i in range(len(self.list)-1):
			self.list[i]=self.list[i+1]
		self.__count-=1
	def show_size(self):
		print(self.__count)

if __name__=="__main__":
	lst1=Queue(3)
	try:
		for i in range(3):
			lst1.push(random.randint(1,9))
		lst1.show()
		for i in range(4):
			lst1.pop()
		lst1.show()
		lst1.show_size()
	except Exception as er:
		print(er)

		
# class Drob():
#     def __init__(self,num,denom):
#         self.num=num
#         self.denom=denom
#
#     # def sum(self,drob2):
#     #     num1=self.num+self.denom*self.full
#     #     num2=drob2.num+drob2.denom*drob2.full
#     #     result_num=num1*drob2.denom+num2*self.denom
#     #     result_denom=self.denom*drob2.denom
#     #     result_full=result_num//result_denom
#     #     result_num=result_num%result_denom
#     #     print(result_full,"\t",result_num,"/",result_denom)
#
#     def show(self):
#         print(self.num,"/",self.denom)
#     #
#     # def dif(self,drob2):
#     #     num1 = self.num + self.denom * self.full
#     #     num2 = drob2.num + drob2.denom * drob2.full
#     #     result_num = num1 * drob2.denom - num2 * self.denom
#     #     result_denom = self.denom * drob2.denom
#     #     result_full = result_num // result_denom
#     #     result_num = result_num % result_denom
#     #     print(result_full, "\t", result_num, "/", result_denom)
#     #
#     # def mul(self,drob2):
#     #     num1 = self.num + self.denom * self.full
#     #     num2 = drob2.num + drob2.denom * drob2.full
#     #     result_num = num1 * drob2.num
#     #     result_denom = self.denom * drob2.denom
#     #     result_full = result_num // result_denom
#     #     result_num = result_num % result_denom
#     #     print(result_full, "\t", result_num, "/", result_denom)
#     #
#     def __sub__(self, drob2):
#         return Drob(
#             (self.num*drob2.denom)-(drob2.num*self.denom),
#             self.denom * drob2.denom
#         )
#
#
#     def __add__(self,drob2):
#         return Drob(
#             self.num*drob2.denom+drob2.num*self.denom,
#             self.denom * drob2.denom
#         )
#
#
#     def __mul__(self, drob2):
#         return Drob(
#             self.num *drob2.num,
#             self.denom * drob2.denom
#         )
#
#
#     def __truediv__(self, drob2):
#         return Drob(
#             self.num * drob2.denom,
#             self.denom * drob2.num
#         )
#
# num1=Drob(1,2)
# num1.show()
# num2=Drob(2,3)
# num2.show()
# (num1+num2).show()
# (num1-num2).show()
# (num1*num2).show()
# (num1/num2).show()

book_id=1
class Book:
    def __init__(self,name,author,publ):
        global book_id
        self.book={book_id:[name, author,publ]}
        book_id+=1
    def show(self):
        print(self.book)
class Library:
    list=[]
    def add(self, book):
        self.list.append(book)

    def show_all(self):
        for i in range(len(self.list)):
            self.list[i].show()

    def remove(self,book):
        return self.list.remove(book)


book1=Book("a","B","acy")
book2=Book("a","B","ac222")
book1.show()
book2.show()
lb=Library()
lb.add(book2)
lb.add(book1)
lb.show_all()
lb.remove(book1)
lb.show_all()



# def check_time(f):
#     def wrapper(list):
#         start=time.time()
#         f(list)
#         end=time.time()-start
#         print(end)
#     return wrapper
#
#
# @check_time
# def foo1(array):
#     for i in array:
#         print(i, end=",")
#     print()
#
# @check_time
# def foo2(array):
#     for i in range(0,len(array),2):
#         print(array[i],end="|")
#     print()
#
#
# list=[random.randint(1,10) for x in range(100)]
# foo1(list)
# foo2(list)

#
# def f(foo):
#     def wrapper(self):
#         print(self.__hash__())
#         foo(self)
#
#     return wrapper
#
#
# class Student:
#     def __init__(self, name, numb):
#         self.name = name
#         self.numb = numb
#
#     @f
#     def show(self):
#         print(self.name, self.numb)
#
#
# st1 = Student("oleg", 123)
# st1.show()

#
# class Figure(ABC):#импортируем абс-абстрактный метод
#     @abstractmethod
#     def getS(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
# class Circle(Figure):
#     def __init__(self,r):
#         self.r=r
#     def  getS(self):
#        return math.pi*self.r**2
#
#     @staticmethod
#     def draw():
#         print("circle")
#
# class Rectangle(Figure):
#     def __init__(self,w,h):
#         self.h=h
#         self.w=w
#     def getS(self):
#         return self.w*self.h
#
#     @staticmethod
#     def draw():
#         print("rectangle")
#
# fig1=Rectangle(2,3)
# fig2=Circle(3)
# fig1.draw()
# print(fig2.getS())


# count=0
# class Student:
#     def __init__(self,name):
#         self.name=name
#         Student.counter()
#     @staticmethod
#     def counter():
#         global count
#         count+=1
# st1=Student("Oleg")
# st2=Student("Alex")
# st3=Student("Oleg3")
# print(count)


class Vegetable(ABC):

    @staticmethod
    def wash():
        print("мою овощ")

    @abstractmethod
    def cook(self):
        pass

class Tomato(Vegetable):
    def __init__(self,m):
        self.m=m

    def cook(self):
        print("готовлю томат")

class Cucumber(Vegetable):
    def __init__(self,m):
        self.m=m


    def cook(self):
        print("готовлю огурец")


ov=Vegetable
tom=Tomato(100)
tom.cook()
cuc=Cucumber(50)
cuc.wash()

