def collatz(x):
    while x > 2:
        s = str(x,"\t->\t")
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
    print(s,1)

collatz(10)
