n = 100
x = 0
i = 1
while i <= n:
    j = i + 1
    while j <= n:
        k = 1
        while k <= j - i:
            x += 1
            print(i, j, k, x)
            k = k + 1
        j = j + 1
    i = i + 1
