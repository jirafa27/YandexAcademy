#https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/kp272sXKd0
#Генератор Фибоначчи

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(*fibonacci(10))

