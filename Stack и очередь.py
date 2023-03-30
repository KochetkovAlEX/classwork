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
