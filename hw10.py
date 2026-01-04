import random
import math

def monte_carlo_integral(f, bounds, num_samples=100000):
    n = len(bounds)
    volume = 1
    for (low, high) in bounds:
        volume *= (high - low)

    total = 0
    for _ in range(num_samples):
        point = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(n)]
        total += f(*point)
    
    return total / num_samples * volume

def unit_sphere_n(*x):
    return 1 if sum(xi**2 for xi in x) <= 1 else 0

if __name__ == "__main__":
    n = 5
    bounds = [(-1, 1)] * n
    num_samples = 1000000

    volume_estimate = monte_carlo_integral(unit_sphere_n, bounds, num_samples)
    print(f"Estimated volume of {n}-D unit sphere: {volume_estimate}")

    exact_volume = math.pi**(n/2) / math.gamma(n/2 + 1)
    print(f"Exact volume of {n}-D unit sphere: {exact_volume}")
