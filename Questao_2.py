def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def fibonacci_sequence(num):
    fib_seq = [0, 1]
    while fib_seq[-1] < num:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if num in fib_seq:
        print(f"{num} pertence a sequencia de Fibonacci.")
    else:
        print(f"{num} nao pertence a sequencia de Fibonacci.")

# Exemplo de uso
num = 47
fibonacci_sequence(num) 
