import random
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
