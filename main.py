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


# crutches solution

def create_sum_list(list_1: list[int], list_2: list[int]) -> list[int]:
    """
    - Принимает списки с целочисленными
    - Подсчитывает сумму соответствующих элементов и кладет в новый список
    - Если списки разной длинны, то недостающие цифры будут ровняться '0'
    - Возвращает новый список
    """
    max_list = max(list_1, list_2, key=len)
    min_list = min(list_1, list_2, key=len)

    result = []
    for num in range(len(min_list)):
        result.append(list_1[num] + list_2[num])

    result += max_list[len(min_list):]
    return result

num_list_1 = [1, 2, 3, 4, 5]
num_list_2 = [10, 20, 30]

print(create_sum_list(num_list_1, num_list_2))
