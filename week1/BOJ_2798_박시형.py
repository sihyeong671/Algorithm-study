# 2798 블랙잭

from random import randint as ri
N = int(input("카드의 개수 : "))
M = ri(3,100000)
print(M)
cardnum = [] # 카드의 값

for i in range(N):
    cardnum.append(ri(3,100000)) # N개의 카드 생성
    # 카드의 값이 중복되지 않게 하려면 ?
print(cardnum)

close = 0 # 가장 가까운 값 저장하는 변수
sum = 0 # 카드 더한 값 저장하는 변수

# 카드가 중복되지 않게 뽑을 경우
for t, i in enumerate(cardnum[0:-2]):
    for z, j in enumerate(cardnum[t + 1:-1]):
        for k in cardnum[t+z+2:]:
            # print(i,j,k)
            sum = i+j+k
            if M - sum >= 0 and sum > close:
                close = sum
                # print(close)
print(close)



