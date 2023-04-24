# 服务中心的最佳位置

sumInput = int(input())
myList = []
for i in range(sumInput):
    myList.append(list(map(int, input().split())))


def execuMath(leftPos, rightPos, Pos):
    if Pos < leftPos:
        return abs(leftPos - Pos)
    elif Pos > rightPos:
        return abs(Pos - rightPos)
    else:
        return 0


minNum = myList[0][0]
maxNum = myList[0][1]
for i in range(len(myList)):
    minNum = min(myList[i][0], minNum)
    maxNum = max(myList[i][1], maxNum)
temp = 0
for k in range(len(myList)):
    temp += execuMath(myList[k][0], myList[k][1], minNum)
outPutNum = temp
for j in range(minNum + 1, maxNum + 1):
    res = 0
    for k in range(len(myList)):
        res += execuMath(myList[k][0], myList[k][1], j)
    outPutNum = min(res, outPutNum)
print(outPutNum)
