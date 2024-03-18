#tabular method of dynamic programming for fibbonacci series
from time import time
# memoizaiton of fibbonacci series
def fibmem(n, mem = None):
    if mem is None: mem = {}
    if n in mem: return mem[n]
    if n <= 2: return 1
    mem[n] = fibmem(n-1, mem) + fibmem(n-2, mem)
    return mem[n]

def fib(n):
    f = {}
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
tic = time()
print(fib(900))
toc = time()

print("Time taken is: ", toc-tic)

tic = time()
print(fibmem(900))
toc = time()
print("Time taken is: ", toc-tic)