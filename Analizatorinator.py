import collections

def count_words(text):
    """Подсчитывает количество слов в тексте"""
    words = text.split() # Разделяем текст на слова по пробелам
    return len(words) # Возвращаем количество слов

def most_common_char(text):
    """Находит самый часто встречающийся символ в тексте исключая пробелы"""
    text_without_spaces = text.replace(" ", "") # Удаляем пробелы
    if not text_without_spaces: # Если текст пустой после удаления пробелов
        return None
    counter = collections.Counter(text_without_spaces) # Считаем символы
    most_common = counter.most_common(1) # Получаем самый частый символ
    return most_common[0][0] # Возвращаем символ

def reverse_words(text):
    """Переворачивает каждое слово в тексте сохраняя порядок слов"""
    words = text.split() # Разделяем текст на слова
    reversed_words = [word[::-1] for word in words] # Переворачиваем каждое слово
    return " ".join(reversed_words) # Объединяем слова обратно в строку

def main():
    """Основной цикл программы"""
    while True:
        text = input("Введите текст (или 'exit' для выхода): ") # Запрашиваем ввод
        if text.lower() == "exit": # Проверяем, хочет ли пользователь выйти
            print("Выход из программы.")
            break
        # Выводим результаты анализа
        print(f"Количество слов: {count_words(text)}")
        common_char = most_common_char(text)
        if common_char:
            print(f"Самый частый символ: '{common_char}'")
        else:
            print("Самый частый символ: текст пустой или состоит только из пробелов")
        print(f"Реверс слов: {reverse_words(text)}")

if __name__ == "__main__":
    main()
