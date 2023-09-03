import numpy as np
a = np.random.randn(5)
print(a)
expa = np.exp(a)
print(expa)
answer = expa / expa.sum()
print(answer)
answer.sum()
print(answer.sum())

A = np.random.randn(100, 5)
print(A)
expA = np.exp(A)

Answer = expA / expA.sum()

print(answer.sum()) 

answer = expA / expA.sum(axis=1, keepdims=True)

print(answer.sum(axis=1))

print(expA.sum(axis=1, keepdims=True))