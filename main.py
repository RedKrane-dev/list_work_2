from itertools import zip_longest


# stackoverflow solution

# def create_sum_list(list_1: list[int], list_2: list[int]) -> list[int]:
#     """
#     - Принимает списки с целочисленными
#     - Подсчитывает сумму соответствующих элементов и кладет в новый список
#     - Если списки разной длинны, то недостающие цифры будут ровняться '0'
#     - Возвращает новый список
#     """
#     result = [sum(nums) for nums in zip_longest(list_1, list_2, fillvalue=0)]
#     return result


# ugly crutches solution

def create_sum_list(list_1: list[int], list_2: list[int]) -> list[int]:
    """
    - Принимает списки с целочисленными
    - Подсчитывает сумму соответствующих элементов и кладет в новый список
    - Возвращает новый список
    """
    result = []
    for num in range(len(list_1)):
        result.append(list_1[num] + list_2[num])
    return result

def min_max_lists(list_1: list[int], list_2: list[int]) -> tuple[list[int], list[int]]:
    """
    - Получает на вход два списка
    - Определяет наименьший и заполняет разницу в длине нулями
    - Возвращает обновленный и не обновленный списки
    - Если списки были одной длины, то ничего не меняет и возвращает их в изначальном виде
    """
    list_1_len = len(list_1)
    list_2_len = len(list_2)

    if list_1_len > list_2_len:
        min_list = list_2
        max_list = list_1
        length_diff = list_1_len - list_2_len
    elif list_1_len < list_2_len:
        min_list = list_1
        max_list = list_2
        length_diff = list_2_len - list_1_len
    else:
        return list_1, list_2

    for zero_num in range(length_diff):
        min_list.append(0)
    return max_list, min_list


num_list_1 = [1, 2, 3, 4, 5]
num_list_2 = [10, 20, 30]

new_list_1, new_list_2 = min_max_lists(num_list_1, num_list_2)

print(create_sum_list(new_list_1, new_list_2))
