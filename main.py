import random
eat = random.randint(0,1)
class Cat:
    global eat
    def __init__(self):
        if eat == 1:
            print('Myav!')
            vubir =input('Eat or dont eat: \n')
            if vubir == 'Eat':
                print('Myr')
            else:
                print('Myav!')
        else:
            print('Myr')
cat = Cat()