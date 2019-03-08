def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    else:
        print (3 * number +1)
        return 3 * number +1

print('Type an integer: ')
try:
    c = int(input())
    while c > 1:
        c = collatz(c)
except ValueError:
    print('You must enter an integer!')
if c <= 0:
    print('You must enter an integer more than 0!')
