from itertools import *
nums = '012345678'
chet = '02468'
a1 = '10'
a2 = '5'

k = 0
for b1 in product(nums, repeat =  2):
    b1 = ''.join(b1)
    for b2 in nums:
        for b3 in chet:
            num = a1+b1+a2+b2+b3
            int_num = int(num)
            if int_num % 1023 == 0:
                print(int_num)
