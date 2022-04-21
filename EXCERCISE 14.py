# Generating  the fibonacchi series up to the Nth term.
import itertools


def fibo(N):
    """ generating fibonacchi python series up to N^th number """
    a = 0
    b = 1
    for i in range(N):
        yield a
        a, b = b, a + b


N = int(input(" enter the number you want to generate fibonacchi series up to:"))
print("your fibonacchi sequence ")
result = list(itertools.islice(fibo(N), N))
print(result)
print("-" * 100)


def squares():
    square = lambda i: i * i
    print("After squaring the numbers of the list:")
    print(list(map(square, result)))


result2 = squares()
print("-" * 100)


def calculateSquareSum(N):
    fibo = [0] * (N + 1);
    if (N <= 0):
        return 0;
    fibo[0] = 0;
    fibo[1] = 1;

    # Initialize result
    # sum = ((fibo[0] * fibo[0]) + (fibo[1] * fibo[1]));
    sum = 1
    # Add remaining terms
    for i in range(2, N + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]);

        sum += (fibo[i] * fibo[i]);

    return sum;


print("Sum of squares of Fibonacci numbers is :",
calculateSquareSum(N));
print("-" * 100)
