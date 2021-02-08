#2231 분해합

N = int(input())
for i in range(N-27,N):
    sum_N = i
    num = str(i)
    for j in num:
        sum_N += int(j)
        if sum_N == N:
            print(i)
            break
    if sum_N == N:
        break
