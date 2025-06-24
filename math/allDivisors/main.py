def find_divisors_optimized(N):
    divisors = []
    sqrt_n = int(math.sqrt(N))
    for i in range(1, sqrt_n + 1):
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
    return sorted(divisors)
