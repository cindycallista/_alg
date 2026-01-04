import random
from math import log2

def cross_entropy(p, q):
    return sum(p[i] * log2(1/q[i]) for i in range(len(p)))

def normalize(q):
    s = sum(q)
    return [x/s for x in q]

p = [0.5, 0.25, 0.25]
q = [1/3, 1/3, 1/3]

steps = 10000
step_size = 0.01

for _ in range(steps):
    i, j = random.sample(range(len(q)), 2)
    delta = random.uniform(-step_size, step_size)
    q_new = q.copy()
    q_new[i] += delta
    q_new[j] -= delta
    q_new = [max(1e-8, x) for x in q_new]
    q_new = normalize(q_new)
    if cross_entropy(p, q_new) < cross_entropy(p, q):
        q = q_new

print("Final q:", q)
print("Cross-entropy H(p, q):", cross_entropy(p, q))
print("Entropy H(p, p):", cross_entropy(p, p))
