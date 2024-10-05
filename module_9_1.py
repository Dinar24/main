# Домашнее задание по теме "Введение в функциональное програмирование"
# Цель: научиться обращаться к функциям, как к обьекту и передавать их в другие
# функции для вызова.
#
# Задача "Вызов разом":
# Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
# int_list - список из чисел (int, float)
# *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим
# из чисел)
# Эта функция должна:
# Вызывать каждую функцию к переданному списку int_list
# Возвращать словарь, где ключом будет название вызванной функции, а значением - её
# результат работы со списком int_list.

def apply_all_func(int_list: list, *functions):
    res_dict: dict ={}
    for func in functions:
        res = func(int_list)
        res_dict[func.__name__] = res
    return res_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))