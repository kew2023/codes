def m(n):
    arr = set()
    arr.add(1)
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            arr.add(i)
            arr.add(n//i)
    mas = sorted(list(arr))
    num = ''
    for i in mas:
        num += str(i)
    return int(num)


k = 0
for x in range(1,1000):
    mx = m(x)
    if mx > 10**9:
        print(mx)
        k += 1
    if k == 5:
        break
