def f(n):
    sprime = 0
    if prime(n): return n

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if prime(i) == True: sprime  += i
            if prime(n//i) == True: sprime += n//i
    return sprime

def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = 100000+1
k = 0
while True:
    strf = str(f(n))
    if len(strf) % 2 == 0 and '7' in strf:
        k += 1
        print(n,strf)
    if k == 5:
        break
    n += 1

