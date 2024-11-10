from datetime import datetime

def age():
    try:
        b = input("Введите дату рождения (дд/мм/гггг): ")
        d = datetime.strptime(b, "%d/%m/%Y")  
        
        t = datetime.today()
        years = t.year - d.year
        months = t.month - d.month
        days = t.day - d.day

        if days < 0:
            months -= 1
            days += (t - datetime(t.year, t.month, 1)).days
        if months < 0:
            years -= 1
            months += 12

        print(f"Ваш возраст: {years} лет, {months} месяцев, и {days} дней.")
    except ValueError:
        print("Ошибка: неверный формат даты. Введите в формате дд/мм/гггг")

age()
