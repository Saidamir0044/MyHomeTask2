# Ex1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ex2
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

# Ex3
def powers_of_two(N):
    k = 1
    while k <= N:
        print(k, end=' ')
        k *= 2
