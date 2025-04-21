import re

def reverse_words(s: str) -> str:
    words = re.split(
        r"[-,.\n?:@]+", s
    )  # Разбиваем строку на элементы массива, убираем лишние символы и оставляем только слова
    return " ".join(words[::-1])


s = "Hello world from Python"
print(reverse_words(s))  # "Python from world Hello"
