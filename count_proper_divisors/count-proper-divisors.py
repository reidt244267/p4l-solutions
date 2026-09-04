# Recitation 1: debugging exercise. Zero points.
#
# A proper divisor of n is a divisor of n other than n itself. The proper
# divisors of 12 are 1, 2, 3, 4 and 6, so count_proper_divisors(12) is 5.
#
# There are two functions below.
#
# brute_count_proper_divisors() is slow, and we have tested it. Trust it.
# count_proper_divisors() is fast, and we have NOT tested it. It is wrong.
#
# Your job is to find out how, using the plan from recitation, in order.
# Do not start by editing the fast function.


def brute_count_proper_divisors(n: int) -> int:
    """
    Count the proper divisors of an integer by checking every candidate.
    Args:
        n: An integer.
    Returns:
        The number of proper divisors of n.
    """
    # a divisor of -n is a divisor of n, so the sign cannot matter
    n = abs(n)

    count = 0
    # every integer from 1 up to n-1 is a candidate divisor
    for d in range(1, n):
        if n % d == 0:
            count += 1
    return count


def count_proper_divisors(n: int) -> int:
    """
    Count the proper divisors of an integer.

    Divisors come in pairs: if d divides n, then so does n // d. So we only
    need to look at candidates up to the square root of n and count both
    members of each pair we find.
    Args:
        n: An integer.
    Returns:
        The number of proper divisors of n.
    """
    n = abs(n)

    
    if n == 1 or n==0:
        return 0

    # 1 is a proper divisor of every n greater than 1, and it pairs with n,
    # which is not a proper divisor, so we count 1 by hand and start at d = 2
    count = 1

    d = 2
    while d * d < n:
        if n % d == 0:
            # d and n // d are both proper divisors
            count += 2
        d += 1

    if d*d==n:
        count+=1

    return count
