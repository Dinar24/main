def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        n = 2
        while n < num and num % n != 0:
            n += 1
        if n == num:
            print('Простое')
        else:
            print('Состовное')
        return num
    return wrapper


@is_prime
def sum_three(a, b, c):
    return sum([a, b, c])


result = sum_three(2, 3, 6)
print(result)