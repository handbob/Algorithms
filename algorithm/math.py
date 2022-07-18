def sum(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s

def positive(n):
    if n <= -1:
        return n * -1
    return n

def negative(n):
    if n >= 0:
        return n * -1
    return n
