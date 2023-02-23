# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/0hIPECwYRI

def same_type(func):
    def wrapper(*args):
        prev_type = type(args[0])
        for arg in args:
            if type(arg) != prev_type:
                print("Обнаружены различные типы данных")
                return False
            prev_type = type(arg)
        return func(*args)
        
    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
