
n = int(input(" enter the number you want prime numbers up to"))

def prime_eratosthenes(n):
    prime_list = []
    not_prime_list = []
    for i in range(2, n+1):
        if i not in not_prime_list:
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                """items which are 2i,3i,n*i are removed upto the number i want the prime numbers"""
                not_prime_list.append(j)

    print(prime_list)
print(" the prime numbers are")
prime_eratosthenes(n)


