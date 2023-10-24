from collections import Counter

def count_common_elements(*lists):
    # Используем Counter для подсчета элементов в каждом из списков
    counters = [Counter(lst) for lst in lists]

    # Используем операцию & для нахождения пересечения множеств элементов в счетчиках
    common_elements = set(counters[0].keys())
    for counter in counters[1:]:
        common_elements &= set(counter.keys())

    # Возвращаем количество общих элементов
    return len(common_elements)


# Пример использования функции
list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 3, 4, 5]
list3 = [3, 4, 4, 5, 6]

count = count_common_elements(list1, list2, list3)
print(f"Количество общих элементов: {count}")


if __name__ == "__main__":
    count_common_elements(list1,list2,list3)
