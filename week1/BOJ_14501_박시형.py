# 14501 퇴사

from random import randint as ri
import time

start = time.time()

N = ri(1,15)
T = []
P = []
money = 0
for i in range(N):
    T.append(ri(1,5))
    P.append(ri(5,1000))
print(T)
print(P)
num = P[:] # shallow copy(새로운 id 할당)
num.append(0)
print(num)
for j in range(N-1, -1, -1):
    if T[j]+j > N:
        num[j] = num[j+1]
        print(num)
    else:
        money = max(num[j+1], P[j]+num[j+T[j]])
        print(money)
        num[j] = money
        print(num)
print(num)
end = time.time()
print(end-start)