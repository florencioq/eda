i = 1
n = 4
soma = 0
while i < n:
    print(i)
    i *= 2
    j = n
    while j > 0:
        print(j)
        j /= 2
        k = j
        while k < n:
            print(k)
            k += 2
            soma += (-j * k)*pow(2,(i / 2))
            print('soma='+str(soma))
