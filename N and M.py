n = int(input())

def sum_dig(x):
    return sum(map(int, str(x)))

min_del = n // 9 if n > 9 else 1

for i in range(min_del, min_del * 100_000):

    if sum_dig(i * n) % n == 0:
        print(f'I got one\n{n * i}')
        break

if i == min_del * 100_000 - 1:
    print('suxx')

