k = 10
i = 1
contagem = primo = n = 0

while i <= k:
    n = 1
    contagem = 0
    print("============")
    print("i: ", i)
    print()
    print("Segundo While")

    while n <= i:
        print("i vale:", i, " --- n vale:", n)
        if i % n == 0:
            contagem += 1
            print("contagem: ", contagem)
        n += 1

    print("=====fim 2 while==")
    print()
    if contagem == 2:
        primo = i

    i += 1
    print("i: ", i, "primo:", primo)

