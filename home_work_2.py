# * Первая часть
age_input = input("Введите ваш возраст: ")
if not age_input.isdigit():
    print("Возраст должен быть положительным числом.")
else:
    temperature_input = input("Введите температуру на улице: ")
    if not temperature_input.lstrip('-').isdigit():
        print("Температура должна быть целым числом.")
    else:
        age = int(age_input)
        temperature = int(temperature_input)
        
        if 20 <= age <= 45 and -20 <= temperature <= 30:
            print("Можно идти гулять")
        elif age < 20 and 0 <= temperature <= 28:
            print("Можно идти гулять")
        elif age > 45 and -10 <= temperature <= 25:
            print("Можно идти гулять")
        else:
            print("Оставайтесь дома")


# * Вторая часть
fruits = ["яблоко", "банан", "апельсин", "манго", "груша"]

index_input = input("Введите индекс фрукта от 0 до 4: ")
if not index_input.isdigit():
    print("Индекс должен быть числом от 0 до 4.")
else:
    index = int(index_input)
    
    if 0 <= index < len(fruits):
        print(fruits[index])
    else:
        print("Неверный индекс")
