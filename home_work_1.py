name = "Ширин"
age = 18
city = "Бишкек"
temperature = 7
square_side = 4
rectangle_length = 10
rectangle_width = 6

print(f"Меня зовут {name}, мне {age} лет.")
print(f"Сегодня в {city} температура {temperature} градусов по Цельсию.")
print(f"Площадь квадрата со стороной {square_side} равна {square_side ** 2}.")
print(f"Периметр прямоугольника со сторонами {rectangle_length} и {rectangle_width} равен {2 * (rectangle_length + rectangle_width)}.")

num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print(f"Тип переменной num_int: {type(num_int)}")
print(f"Тип переменной num_float: {type(num_float)}")

user_name = input("Введите ваше имя: ")
user_age = int(input("Введите ваш возраст: "))
user_city = input("Введите ваш город: ")

birth_year = 2024 - user_age 
print(f"Привет, {user_name}! Тебе {user_age} лет, ты родился в {birth_year} году и ты живешь в городе {user_city}.")
