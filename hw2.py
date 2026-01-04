cache = [None] * 100000
calls = 0

def pow_direct(n):
    global calls
    calls += 1
    return 2 ** n

def pow_recursive_sum(n):
    global calls
    calls += 1
    if n == 0:
        return 1
    return pow_recursive_sum(n - 1) + pow_recursive_sum(n - 1)

def pow_recursive_mul(n):
    global calls
    calls += 1
    if n == 0:
        return 1
    return 2 * pow_recursive_mul(n - 1)

def pow_memo(n):
    global calls
    calls += 1
    if n == 0:
        return 1
    if cache[n] is not None:
        return cache[n]
    cache[n] = pow_memo(n - 1) + pow_memo(n - 1)
    return cache[n]

print(pow_direct(10), f"calls={calls}")
calls = 0
print(pow_recursive_sum(10), f"calls={calls}")
calls = 0
print(pow_recursive_mul(10), f"calls={calls}")
calls = 0
print(pow_memo(10), f"calls={calls}")
