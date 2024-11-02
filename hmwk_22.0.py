def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        for j in range(len(i)):
            try:
                result = result + i[j]
            except TypeError as exc:
                print(f'{i[j]} - ошибка, {incorrect_data + 1} - количество ошибок')
            incorrect_data += 1
            continue

    return tuple((result, incorrect_data))


def calculate_average(*numbers):
    results_sum = 0
    try:
        results = personal_sum(*numbers)
        for line in numbers:
            for i in range(len(line)):
                if type(line[i]) == int or type(line[i]) == float:
                    results_sum += 1
            results_sum = results[0] / results_sum
    except ZeroDivisionError as exc:
        print(f'При делении на ноль - {0}, ошибка - {exc}')
    except TypeError as exc_2:
        print(f'В numbers записан некорректный тип данных {exc_2} - {None}')

    return results_sum


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average(["Строка", 1, 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
