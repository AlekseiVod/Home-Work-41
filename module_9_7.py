# Функция декоратор которая распечатывает "Простое",
# если результат 1ой функции будет простым числом
# и "Составное" в противном случае
def is_prime(func):
    def wrapper(*args):

        result_dec = func(*args)
        if result_dec < 2:
            print("Составное")
            return result

        for i in range(2, int(result_dec ** 0.5) + 1):
            if result_dec % i == 0:
                print("Составное")
                return result
            print("Простое")
            return result_dec

    return wrapper


# Функция, которая складывает 3 числа
@is_prime
def sum_three(a, b, c):
    return a + b + c


# Вывод результата
result = sum_three(2, 3, 6)
print(result)
