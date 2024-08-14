def print_params(a=1, b = 'string', c = True):
    print(a, b, c)
    

print_params(3)
print_params(3, 5)
print_params()
print_params(b = 25)
print_params([1, 2, 3])

values_list =[False, 5, 'string2']
values_dict ={'a': True, 'b': 25.3, 'c': 777} 

print()
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [11.22, 'string3']

print()
print(*values_list_2, 42)