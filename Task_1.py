# Напишите прогамму, которая принимает на вход число N
# и выдает последовательность из N членов.

print('Olga')
user = int(input())
res = 1
for i in range(user):
    print(res, end=' ')
    res *= -3
