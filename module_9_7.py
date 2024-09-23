# Функция декоратор которая распечатывает "Простое",
# если результат 1ой функции будет простым числом
# и "Составное" в противном случае
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 1:
            print("Составное")  # Учитываем, что ноль и отрицательные числа не простые
            return result

        # Проверка на простое число
        if result == 1:
            print("Составное")
            return result

        prime = True
        for j in range(2, result):
            if result % j == 0:
                prime = False
                break

        if prime:
            print("Простое")
        else:
            print("Составное")

        return result

    return wrapper


# Функция, которая складывает 3 числа
@is_prime
def sum_three(a, b, c):
    return a + b + c


# Вывод результата
print(sum_three(2, 3, 6))  
