import numpy as np

N = 1000000  # Number of random matrices sampled
count = 0


for i in range(N):
    A = np.random.randint(-25, 25, (3, 3))
    if round(np.linalg.det(A)) == 1 or round(np.linalg.det(A))==-1:     
        count += 1
        print(A)

print(count/N*100)

