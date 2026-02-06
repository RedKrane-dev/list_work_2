num_list_1 = [1, 2, 3, 4]
num_list_2 = [10, 20, 30]

def create_sum_list(list_1: list[int], list_2: list[int]) -> list[int]:
    """
    - Принимает списки с целочисленными
    - Определяет минимальную длину списков
    - Подсчитывает сумму соответствующих элементов и кладет в новый список
    - Возвращает новый список
    """
    min_len = min(len(list_1), len(list_2))
    result = []
    for num in range(min_len):
        result.append(num_list_1[num] + num_list_2[num])

    return result

print(create_sum_list(num_list_1, num_list_2))
