def sum_of_moduli(complex_numbers: list) -> float:
    # Ваш код здесь
    return sum(abs(num) for num in complex_numbers)

# Тест
complex_numbers = [complex(3, 4), complex(1, 1), complex(0, 2)]
print(f'{sum_of_moduli(complex_numbers):.1f}')  # 8.4
