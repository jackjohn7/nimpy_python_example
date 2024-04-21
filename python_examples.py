#!/usr/bin/env python3

def n_fib_iter(n: int) -> int:
    """Calculate the nth fibonacci number iteratively."""
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, b + a
    return b


def n_fib_rec(n: int) -> int:
    """Calculate the nth fibonacci number recursively."""
    if n == 0 or n == 1:
        return n
    return n_fib_rec(n-1) + n_fib_rec(n-2)


def is_prime(n: int) -> bool:
    """Determine whether a number is prime."""
    upper_bound = int((n ** 0.5) // 1)
    for i in range(1, upper_bound + 1):  # inclusive
        if n % i == 0:
            return False
    return True


def is_prime_2(n: int) -> bool:
    """Detmine whether a number is prime."""
    if n == 2 or n == 3:
        return True
    return n == 2 or n == 3 or (n+1) % 6 == 0 or (n-1) % 6 == 0


def n_prime(n: int) -> int:
    """Calculate the nth prime number."""
    i = 2
    prime = 2
    while n > 0:
        if is_prime_2(i):
            prime = i
            n -= 1
        i += 1
    return prime
