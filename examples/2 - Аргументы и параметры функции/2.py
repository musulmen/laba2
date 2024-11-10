def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}

my_cat = cat('Alise', 'Grey', 9)
print(my_cat)

my_cat_kw = cat(color='Grey', age=9, name='Alise')
print(my_cat_kw)
