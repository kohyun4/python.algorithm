# 백준 문제 2630
# https://www.acmicpc.net/problem/2630

N = int(input()) # N = 2, 4, 6, 8, 16, 32, 64, 128
# N = 8

R = []
for i in range(N):
    Rr = list(map(int, input().split(' ')))
    R.insert(i, Rr)
"""
R = [[1, 1, 0, 0, 0, 0, 1, 1],
     [1, 1, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 1, 1, 1, 1],
     [0, 1, 0, 0, 1, 1, 1, 1],
     [0, 0, 1, 1, 1, 1, 1, 1],
     [0, 0, 1, 1, 1, 1, 1, 1]]
"""

def checkArr(arr):
    n = len(arr)
    sum = 0
    mul = 1
    for i in range(n):
        for j in range(n):
            sum += arr[i][j]
            mul *= arr[i][j]

    if sum == 0:
        return 0
    elif mul == 1:
        return 1
    else:
        return 2

numW = 0
numB = 0
def divArr(arr):
    global numW, numB
    if checkArr(arr) == 0:
        numW += 1
        return numW, numB
    elif checkArr(arr) == 1:
        numB += 1
        return numW, numB
    else:
        n = len(arr)
        dn = int(n / 2)
        arr1, arr2, arr3, arr4 = [], [], [], []
        for i in range(dn):
            arr1.append(arr[i][0:dn])
            arr2.append(arr[i][dn:n])
            arr3.append(arr[dn + i][0:dn])
            arr4.append(arr[dn + i][dn:n])
        divArr(arr1)
        divArr(arr2)
        divArr(arr3)
        divArr(arr4)

divArr(R)
print(numW)
print(numB)
