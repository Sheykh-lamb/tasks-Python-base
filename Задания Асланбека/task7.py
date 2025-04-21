def clean_file(input_file: str, output_file: str) -> None:
    with open(
        input_file, "r", encoding="utf-8"
    ) as infile:  # открывем файл, будет обращаться к нему как к infile
        text = infile.readlines()  # считаем строки
    print(text)
    cleaned_text = [line for line in text if line.strip() != ""] # Убираем все пустые строки и строки только с пробелами
    print(cleaned_text)
    with open(output_file, "w", encoding="utf-8") as outfile: #создаем и записываем в новый файл 
        outfile.writelines(cleaned_text)


# Тест
input_file = "input.txt"
output_file = "output.txt"
clean_file(input_file, output_file)