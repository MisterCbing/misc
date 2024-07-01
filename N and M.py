n = int(input())

def sum_dig(x):
    return sum(map(int, str(x)))

for i in range(1, 100_000_000):

    if sum_dig(i * n) % n == 0:
        print(f'I got one\n{n * i}')
        break

if i == 99_999_999:
    print('suxx')
