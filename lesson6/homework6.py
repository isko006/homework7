import random

num = random.randint(1,16)

user_num=-3

while True:

  while user_num!=num:

    user_num=int(input("Угадай число от 1 до 15"))

    if user_num > num:

        print('число должно быть меньше!')

    elif user_num < num:

        print('число должно быть больше')

    else:

        print('вы угодали это число = ' + str(num))

     #Конец игры - выйти из цикла whaile

    break
