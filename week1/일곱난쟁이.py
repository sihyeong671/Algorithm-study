#아홉 난쟁이의 키는 모두 다르다

# 랜덤수로 하기

# 입력으로 하기


height = []
for i in range(9):
    height.append(int(input()))
    print(height)

for i in range(8):
    for j in range(i+1,9):
        if sum(height) - height[i] - height[j] == 100:
            height.pop(i)
            height.pop(j-1)
            height.sort()
            print(height)
            exit()

