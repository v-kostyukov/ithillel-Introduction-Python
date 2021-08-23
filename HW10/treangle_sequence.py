def count_first(nums, n):
    nums = 1
    k = 0
#    for i in range(1, n + 1):
#        print(k)
#        if i == k * (k + 1) // 2:
#            k += 1
    # return k
    for i in range(n):
        print(nums, end=' ', flush=True)
        k = k + 1
        if k == nums:
            k = 0
            nums = nums + 1
    print()


k1 = 1
n1 = int(input('Введите число n: '))
print(count_first(k1, n1))


