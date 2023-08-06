def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            next_num = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_num)
        return fib_seq

n = 10
fib_seq = fibonacci_sequence(n)
print(fib_seq)
