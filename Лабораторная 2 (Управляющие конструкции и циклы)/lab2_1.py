city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]


# TODO найдите количество городов в списке
num_cities = len(city_list)


# TODO найдите общее количество населения
total_population = sum(
    [city["population"] for city in city_list]
)  # находим общую популяцию в одну строку через list comprehension

"""" На самом деле тут не всегда это лучшее решение. Если у нас city_list содержал бы 'миллиард' значений, весил бы очень много
     и на исполнительной машине было бы мало свободного места, то неявно создавать отдельный список с населением ради нахождения 
     суммы не лучшая идея, потому что память бы быстро закончилась. Но в наших обычных жизненных примерах почему бы и нет   """

# TODO распечатайте среднее арифметическое населения
print(f"Среднее арифметическое населения равно = {total_population/num_cities}")
