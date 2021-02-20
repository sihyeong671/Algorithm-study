# 2747 피보나치 수
arr = [0,1] # 0번째, 1번째

n = int(input()) #n 입력 (n번째)

for i in range(2,n+1):
    arrnum = arr[i-2] + arr[i-1]
    arr.append(arrnum)
k = arr.pop()
print(k)