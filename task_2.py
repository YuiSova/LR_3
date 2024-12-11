# TODO Напишите функцию find_common_participants
def find_common_participants(first_str, second_str, separator=','):
    first_set = set(first_str.split(separator))
    second_list = second_str.split(separator)
    result_list = list(first_set.intersection(second_list))
    result_list.sort()
    return result_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))# TODO Провеьте работу функции с разделителем отличным от запятой