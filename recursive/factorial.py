def Fibonacci(n, memo = {}):
    
    print("leel--->", n , memo)
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = n
        return n
        
    memo[n] = Fibonacci(n-1,memo) + Fibonacci(n-2,memo) 
    
    return memo[n]
        
    
print(Fibonacci(6))
