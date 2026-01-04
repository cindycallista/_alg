def f(x):
    return x*x - 4*x + 3

def df(x):        
    return 2*x - 4

def gradient_descent(start_x, lr=0.1, iterations=50):
    x = start_x
    for _ in range(iterations):
        x = x - lr * df(x)
    return x, f(x)

if __name__ == "__main__":
    x, fx = gradient_descent(start_x=5)
    print("Best x =", x)
    print("f(x)   =", fx)
