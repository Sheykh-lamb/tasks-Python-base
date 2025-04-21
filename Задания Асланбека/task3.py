def char_frequency(s: str) -> dict:
    text = " ".join(s).split()
     
    dict1 = dict.fromkeys(text, 0)
    for symbol in s:
        dict1[symbol] = dict1.get(symbol,0) + 1
    return dict1


# Тест
s = "abracadabra"
print(char_frequency(s))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
