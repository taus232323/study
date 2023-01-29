numbers = []
for i in range(10):
    i = int(input('Введите любое число: '))
    numbers.append(i)
numbers.sort()
for a in numbers:
    a *= 10
    print(a)


