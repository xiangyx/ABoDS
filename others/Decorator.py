import numpy as np
import time

def display_time(func):
    def wrapper(*args):
        t0 = time.time()
        res = func(*args)
        print(f"Total time: {time.time() - t0:.4f}s")
        return res
    return wrapper


def normal_mixture(mu, sigma, p):
    n1 = np.random.normal(mu[0], sigma[0], 1)
    n2 = np.random.normal(mu[1], sigma[0], 1)
    return p * n1 + (1 - p) * n2

@display_time
def print_normalmix2():
    for i in range(100):
        print(f"i = {i + 1}: {normal_mixture(mu, sigma, p)[0]:.4f}")

@display_time
def count_normalmix2_01(n_sim, mu, sigma, p):
    count = 0
    for i in range(n_sim):
        n = normal_mixture(mu, sigma, p)[0]
        if n >= 0 and n <= 1:
            count += 1
    return count


mu = np.array([0, 1])
sigma = np.array([2, 4])
p = 0.8
n_sim = 100
# print_normalmix2()
count = count_normalmix2_01(n_sim, mu, sigma, p)
print(count)