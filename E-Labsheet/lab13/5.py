n = int(input(""))
char = input("")

if n < 0 or char not in ['e', 'E', 'o', 'O']:
    print("ERROR")
else:
    fib = [0] * (n + 1)
    fib[0] = 1
    if n > 0:
        fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    total = 0
    if char in ['e', 'E']:
        for i in range(0, n + 1, 2):
            total += fib[i]
    elif char in ['o', 'O']:
        for i in range(1, n + 1, 2):
            total += fib[i]

    print(total)