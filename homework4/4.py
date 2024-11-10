import random

while True:
    def find_multiples():
        try:
            x = int(input("Введите цифру: "))
            if x == 0:
                print("Ошибка: ноль кратен любому числу.")
                return
            if not 1 <= x <= 9:
                print("Ошибка: введите цифру от 1 до 9.")
                return
            
            nums = [random.randint(0, 200) for _ in range(10)]
            print("Сгенерированный список чисел:", nums)

            multiples = list(filter(lambda n: n % x == 0, nums))
            print("Числа, кратные", x, ":", multiples)
        
        except ValueError:
            print("Ошибка: введите цифру от 1 до 9.")
    find_multiples()
    
