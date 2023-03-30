# class Student:
#     name="Noname"
#     group="0"
#
#     def show_info(self):#передаем объект, с которым работаем
#         print(f" name: {self.name} | group: {self.group}")#self. = обращение
#
# st1=Student()
# st1.name="Alex"
# st1.group="A2"
# st1.show_info()
#
# class Machine:
#     def __init__(self,color,model):#коструктор. передача объектов
#         self.model=model
#         self.color=color
#     def show_info(self):
#         print(f'цвет {self.color} | марка {self.model}')
#
#     def change_color(self, color):
#         self.color=color
#
# car1=Machine("red","Lada")
# car1.show_info()
# car1.color="red"
# car1.vEngine=2.5
# car1.show_info()


#
# class Cat():
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#         print("create",self)
#
#     def __del__(self):
#         print(f"{self.name} убит")
#
#     def sleep(self):
#         print(f"{self.name} спит")
#     def show_info(self):
#         print(f"{self.name} | {self.weight}")
#
# cat2=Cat("Cat2",10)
# cat2.sleep()
# cat2.show_info()
#
# class Drob():
#     def __init__(self,full,num,denom):
#         self.full=full+num//denom
#         self.num=num%denom
#         self.denom=denom
#     def sum(self,drob2):
#         num1=self.num+self.denom*self.full
#         num2=drob2.num+drob2.denom*drob2.full
#         result_num=num1*drob2.denom+num2*self.denom
#         result_denom=self.denom*drob2.denom
#         result_full=result_num//result_denom
#         result_num=result_num%result_denom
#         print(result_full,"\t",result_num,"/",result_denom)
#     def show(self):
#         print(self.full,"\t",self.num,"/",self.denom)
#
#
# num1=Drob(1,2,5)
# num1.show()
# num2=Drob(0,1,2)
# num2.show()
# num1.sum(num2)

# class Item():
#     def __init__(self,type,price):
#         self.type=type
#         self.price=price
#
#
# class Shop():
#     list=[]
#     pribil=0
#     def __init__(self,money):
#         self.money=money
#
#     def buy(self,item):
#         if self.money>=item.price:
#             self.list.append(item.type)
#             self.money-=item.price
#     def sell(self,item):
#         for i in self.list:
#             if item == i.item:
#                 self.pribil+=i.price*2.2
#                 self.list.remove(i)
#
#
#
#
#
# shop1=Shop(1000)
# tovar1=Item("Tomat",10)
#
# print(shop1.sell(tovar1))
# shop1.buy(tovar1)
# print(shop1.money)
# print(shop1.pribil)

