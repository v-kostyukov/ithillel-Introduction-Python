# def count_first(n, k=1,):
#     if not n:
#         return
#     for _ in range(k):
#         print(k, end=' ')
#     count_first(n - 1, k + 1)

def count_first(n, nums=1,):
    # nums = 1
    k = 0
    #  for i in range(1, n + 1):
    #      print(k)
    #      if i == k * (k + 1) // 2:
    #            k += 1
    #  return k
    for i in range(n):
        print(nums, end=' ', flush=True)
        k = k + 1
        # if k == nums:
        #    k = 0
        #    nums = nums + 1
        return count_first(n - 1, nums=nums + 1) if (k == nums) else count_first(n+1, nums=nums + 1)
    # for i in range(1, n + 1):
    # return count_first(1, n)


# n = int(input('Введите число n: '))
# print(count_first(n))
count_first(int(input('Введите число n: ')))

