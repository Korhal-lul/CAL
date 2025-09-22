import random
import matplotlib.pyplot as plt
import numpy as np

def bsearch(v, target): 
    n = len(v)
    l = 0 #leftmost
    r = n-1 #rightmost
    m = int((l+r)/2) #middle
    i = 0 #num of iterations

    while l <= r:
        i+=1
        if v[m] == target:
            return i
        if v[m] < target:
            l = m+1
        if v[m] > target:
            r = m-1
        m = int((l+r)/2)
    return i

def linear(v, target):
    i = 0
    while v[i] != target:
        i+=1
    return i

# Define the range of array sizes to test
array_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 50000, 100000]
iterations_per_size = 100  # Number of searches to average for each array size

# Lists to store average iterations for each algorithm
avg_bsearch_iterations = []
avg_linear_iterations = []

print("Testing different array sizes...")

for n in array_sizes:
    bsearch_total = 0
    linear_total = 0
    
    for _ in range(iterations_per_size):
        # Generate sorted random array
        vetor = [random.randint(-10000, 10000) for _ in range(n)]
        vetor.sort()
        
        # Choose a random target from the array
        target = random.choice(vetor)
        
        # Count iterations for both algorithms
        bsearch_total += bsearch(vetor, target)
        linear_total += linear(vetor, target)
    
    # Calculate averages
    avg_bsearch_iterations.append(bsearch_total / iterations_per_size)
    avg_linear_iterations.append(linear_total / iterations_per_size)
    
    print(f"Size: {n}, Binary Search Avg: {avg_bsearch_iterations[-1]:.2f}, Linear Search Avg: {avg_linear_iterations[-1]:.2f}")

# Plot the results
plt.figure(figsize=(12, 8))

# Plot binary search
plt.plot(array_sizes, avg_bsearch_iterations, 'bo-', label='Binary Search', linewidth=2, markersize=6)

# Plot linear search
plt.plot(array_sizes, avg_linear_iterations, 'ro-', label='Linear Search', linewidth=2, markersize=6)

# Add logarithmic scale for better visualization of exponential growth
plt.xscale('log')
plt.yscale('log')

# Customize the plot
plt.xlabel('Number of Elements (log scale)', fontsize=12)
plt.ylabel('Average Iterations (log scale)', fontsize=12)
plt.title('Search Algorithm Performance: Elements vs Iterations', fontsize=14)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

plt.tight_layout()
plt.savefig("test.png")
plt.show()