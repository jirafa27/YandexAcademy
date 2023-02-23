# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/6O4mmgt83M

# Реализуйте декоратор result_accumulator, который модернизирует
# функцию с неопределенным количеством позиционных параметров
# следующим образом:
# Добавляет именованный параметр method со значением по умолчанию accumulate;
# При вызове функции с параметром method равным accumulate,
# результат сохраняется в очередь
# (для каждой функции в собственную),
# а функция ничего не возвращает;
# При вызове функции с параметром method равным drop,
# возвращается все накопленные результаты, а очередь сбрасывается.

def result_accumulator(func):
    k = []
    
    def wrapper(*args, method='accumulate'):
        if method == 'accumulate':
            return k.append(func(*args))
        else:
            k.append(func(*args))
            lst = list(k)
            k.clear()
            return lst
    
    return wrapper


print("Test1-----------------------------------")

@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))

print()
print("Test2-----------------------------------")


@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
