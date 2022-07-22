from itertools import *
nums = '012345678'
a1 = '10'
a2 = '0'

k = 0
for i in range(3+1):
    for b1 in product(nums, repeat =  i):
        b1 = ''.join(b1)
        for b2 in nums:
            num = a1+b1+a2+b2
            if num[0] != '0':
                int_num = int(num,9)
                if int_num % 21 == 0:
                    k += 1
print(k)
