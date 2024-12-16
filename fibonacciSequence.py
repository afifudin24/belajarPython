def fibonacci(n):
    fib_sequence = []  # Array untuk menyimpan angka Fibonacci
    
    def fib_helper(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return fib_helper(x-1) + fib_helper(x-2)
    
    # Mengisi array dengan angka Fibonacci
    for i in range(n):
        fib_sequence.append(fib_helper(i))
    
    return fib_sequence

print(fibonacci(7))
