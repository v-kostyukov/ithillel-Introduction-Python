# def count_first(n, k=1,):
#     if not n:
#         return
#     for _ in range(k):
#         print(k, end=' ')
#     count_first(n - 1, k + 1)

def count_first(n: int) -> str:
    k = 1
    res = ''
    for i in range(1, n + 1):
        res = ' '.join([res, str(k)])
        if i == k * (k + 1) // 2:
            k += 1
    return res


n = int(input('Введите число n: '))
print(count_first(n))

