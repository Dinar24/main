numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # простое
not_primes = [] # не простое

is_prime = True # простое число или нет (пока содержит - True)

for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
    else:
            is_prime = True
            primes.append(i)
            
print("Primes", primes)
print("Not_primes", not_primes)