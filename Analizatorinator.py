import collections

def count_words(text):
    """подсчитывает количество слов в тексте"""
    return len(text.split())
def most_common_char(text):
    """находит самый часто встречающийся символ в тексте исключая пробелы"""
    counter = collections.Counter(text.replace(' ', ''))
    if counter:
        return counter.most_common(1)[0][0]
    return None  # если текст пустой или состоит только из пробелов
def reverse_words(text):
    """переворачивает каждое слово в тексте сохраняя порядок"""
    return ' '.join(word[::-1] for word in text.split())

def main():
    """основной цикл программы"""
    while True:
        text = input("Введите текст (или 'exit' для выхода): ")
        if text.lower() == 'exit':
            print("Выход из программы.")
            break
        print(f"Количество слов: {count_words(text)}")
        common_char = most_common_char(text)
        if common_char:
            print(f"Самый частый символ: '{common_char}'")
        else:
            print("Самый частый символ: текст пустой или состоит только из пробелов")
        print(f"Реверс слов: {reverse_words(text)}")

if __name__ == '__main__':
    main()