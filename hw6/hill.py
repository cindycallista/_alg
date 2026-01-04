import random

def f(x):
    return x*x - 4*x + 3

def hill_climbing(start_x, step=0.1, iterations=50):
    x = start_x
    for _ in range(iterations):
        left = x - step
        right = x + step

        if f(left) < f(x):
            x = left
        elif f(right) < f(x):
            x = right
        else:
            break   
    return x, f(x)

if __name__ == "__main__":
    x, fx = hill_climbing(start_x=5)
    print("Best x =", x)
    print("f(x)   =", fx)
