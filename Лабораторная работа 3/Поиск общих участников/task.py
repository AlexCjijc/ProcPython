# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, separator=','):
    common = set(str1.split(separator)).intersection(set(str2.split(separator)))
    common = list(common)
    common.sort()
    return common
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
