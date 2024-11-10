def my_generate(start=0, stop=30, step=1):
    number = start
    while number <= stop:
        yield number
        number += step

def get_odd_numbers():
    for num in my_generate(1, 29, 2):
        yield num

ranger = get_odd_numbers()

numbers = list(ranger)

print("Первое значение:", numbers[0])
print("Пятое значение:", numbers[4])
print("Последнее значение:", numbers[-1])
