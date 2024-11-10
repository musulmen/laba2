def get_number():
    for num in range(1, 29, 2):
        yield num

n = list(get_number())

print("Первое значение:", n[0])
print("Пятое значение:", n[4])
print("Последнее значение:", n[-1])
