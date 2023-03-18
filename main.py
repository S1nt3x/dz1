# import random
# eat = random.randint(0,1)
# class Cat:
#     global eat
#     def __init__(self):
#         if eat == 1:
#             print('Myav!')
#             vubir =input('Eat or dont eat: \n')
#             if vubir == 'Eat':
#                 print('Myr')
#             else:
#                 print('Myav!')
#         else:
#             print('Myr')
# cat = Cat()
# time = 0
# time1 = time/30
# money = 10000
# work = input('працювати чи отримувати стипендію: ')
# while True:
#     if time < 365:
#         time += 1
#         money -= 200
#         if work == 'працювати':
#             money += 20000
#         elif work == 'отримувати стипендію':
#             money += 10000
#     elif time == 365:
#         if money <= 0:
#             print(f'У тебе кредит на {int(-1*money)}')
#         else:
#             print(f"Вітаю!Ти прожив!На доступні кошти ({money}) можеш відпочити")
# class PC:
#  def __init__(self, cpu, gpu, ram, ssd, power_unit, motherboard):
#   self.cpu = cpu
#   self.gpu = gpu
#   self.ram = 16
#   self.ssd = 512
#   self.power_unit = 650
#   self.motherboard = 'Assus'
#  def get_into(self):
#   return f'CPU = {self.cpu}\n' \
#          f'Mother = {self.motherboard}\n' \
#          f'GPU = {self.gpu}\n' \
#          f'RAM = {self.ram}GB' \
#          f'SSD = {self.ssd} GB' \
#          f'Power = {self.power_unit} w'
#pc1 = PC('i','3', 16, 512, 650, 'Asus')
#pc2 = PC('i3', '1090', 8, 512, 600, 'Asus')
#print(pc1.get_into())# print(pc2.get_into())
#class Person:
#   def __init__(self, height, mass, age, hair, money=15000):
#     self.height = height
#     self.mass = mass
#     self.age = age
#     self.hair = hair
#     self.money = money
#   def get_into(self):
#     return f'Height = {self.height}cm\n' \
#            f'Streing = {self.mass}kg\n' \
#            f'Age = {self.age}\n' \
#            f'Hair = {self.hair}\n' \
#            f'Money = {self.money}\n'
#  def take_money(self,amound):
#    if self.money > amound > 0:
#      if self.money > 0:
#        print(f'Your money: {amound}')
#      else:
#        print('Недостатньо')
#   else:
#      print("Недостатньо")
#
#
#
#
#
#person1 = Person(180, 75, 20, 'dark')
#
#person2 = Person(200, 90, 25, 'white')
#
#
#print(person1.take_money(10000))

# from random import randint

# class User:
#     HINTS = {
#         'Grate': 0, 'Close': 20, "Not bad": 40, 'Quiet bad': 100 }
#
#     def __init__(self, name):
#         self.name = name
#         self.choice1 = 0 self.__choice = 0 self.__score = 0 self.__wins = 0 def __str__(self):
#         return f'name: {self.name}\n choise: {self.__choice}score: {self.__score}\n wins: {self.__wins}' def add_score(self):
#         pass def set_choice(self, answer):
#         self.__choice = answer
#
#     def get_choice(self):
#         return self.__choice
#
#     def status_round(self, number):
#         for key, value in self.HINTS.items():
#             if number <= value:
#                 self.choise1 = self.__choice - abs(rand_num)
#                 print(self.choise1)
#
#
# a = User('Nick')
# b = User('Joe')
#
#
# rand_num = randint(0, 100)
# print()
#
# for i in range(3):
#     a.set_choice(int(input(f'{a.name}, enter answer:')))
#     b.set_choice(int(input(f'{b.name}, enter answer:')))
#     print(abs(a.get_choice() - rand_num))
#     print(abs(b.get_choice() - rand_num))