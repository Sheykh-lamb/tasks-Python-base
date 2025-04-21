def are_anagrams(s1: str, s2: str) -> bool:
    # Создаем два массива и инициализируем их ASCII значениями символов
    array_s1 = [ord(symbol) for symbol in s1] 
    array_s2 = [ord(symbol) for symbol in s2]

    if len(s1) == len(s2) and sum(array_s1) == sum(array_s2):
        return True
    else:
        return False

# Тест 1 
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # True



# Вариант 2 если в словах будут заглавные буквы
def are_anagrams_2(s1: str, s2: str) -> bool:
    # Создаем два массив и инициализируем их ASCII значениями символов, делаем все буквы строчными
    array_s1 = [ord(symbol.lower()) for symbol in s1] 
    array_s2 = [ord(symbol.lower()) for symbol in s2]

    if len(s1) == len(s2) and sum(array_s1) == sum(array_s2):
        return True
    else:
        return False
    
# Тест 2 
s1 = "Listen"
s2 = "silent"
print(are_anagrams_2(s1, s2))  # True   