city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

max_population = 5  # Пороговое значение для населения

"""" Если мы решаем через list comprehension, то мы в любом случае создаём новый список. Лучше не менять 
     уже существующий city_list, а сделать filtered_cities с городами, где популяция меньше порогового значения для 
     населения. И затем вывести длинну данного списка"""

filtered_cities = [city for city in city_list if city["population"] < 5]


print(f"Количество городов с население до 5 млн. жителей равно = {len(filtered_cities)}")
