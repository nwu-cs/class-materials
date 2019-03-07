def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def lucas(n):
    return 0

memoF = {0:0, 1:1}
def fib_M(n):
    return 0

memoL = {?????}
def lucas_M(n):
    return 0



if __name__ == '__main__':
    for i in range(1, 40):
        print(i, fib(i), lucas(i))
