import random
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
time = 0
time1 = time/30
money = 10000
work = input('працювати чи отримувати стипендію: ')
while True:
    if time < 365:
        time += 1
        money -= 200
        if work == 'працювати':
            money += 20000
        elif work == 'отримувати стипендію':
            money += 10000
    elif time == 365:
        if money <= 0:
            print(f'У тебе кредит на {int(-1*money)}')
        else:
            print(f"Вітаю!Ти прожив!На доступні кошти ({money}) можеш відпочити")