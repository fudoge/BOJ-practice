def fibo_with_DP(n):
    cache = {}
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            cache[n] = n
            return cache[n]
        else:
            cache[n] = fibo_with_DP(n-1) + fibo_with_DP(n-2)
            return cache[n]
        
print(fibo_with_DP(20))