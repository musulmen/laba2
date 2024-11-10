import random

def game():
    opts = ['камень', 'ножницы', 'бумага']
    
    while True:
        user = input("Выберите (1 - камень, 2 - ножницы, 3 - бумага): ")
        while user not in ['1', '2', '3']:
            print("Некорректный выбор. Попробуйте снова.")
            user = input("Выберите (1 - камень, 2 - ножницы, 3 - бумага): ")

        user_choice = opts[int(user) - 1]
        comp = random.choice(opts)
        print(f"Компьютер выбрал: {comp}\n")

        if user_choice == comp:
            print("Ничья!\n")
        elif (user_choice == 'камень' and comp == 'ножницы') or \
             (user_choice == 'ножницы' and comp == 'бумага') or \
             (user_choice == 'бумага' and comp == 'камень'):
            print("Вы победили!\n")
        else:
            print("Вы проиграли))))))\n")
game()
