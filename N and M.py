n = int(input())

def sum_dig(x):
    return sum(map(int, str(x)))

min_del = int((n // 9 if n > 9 else 1) * '9')

for i in range(min_del, min_del * 1000):

    if sum_dig(i * n) % n == 0:
        print(f'I got one\n{n * i}')
        break

if i == min_del * 1000 - 1:
    print('suxx')

