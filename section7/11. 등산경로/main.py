'''

클래스 명 : Ch 11

설명 : 등산경로 입니다.

작성일 : 2022.05.30

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
등산을 매우 좋아하는 철수는 마을에 있는 뒷산에 등산경로를 만들 계획을 세우고 있습니다. 
마을 뒷산의 형태를 나타낸 지도는 N*N 구역으로 나뉘어져 있으며, 각 구역에는 높이가 함께 나타나 있습니다.
어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동할 수 있도록 등산로를 설계하려고 합니다. 
등산로의 출발지는 전체 영역에서 가장 낮은 곳이고, 목적지는 가장 높은 곳입니다. 
출발지와 목적지는 유일합니다. 지도가 주어지면 출발지에서 도착지로 갈 수 있는 등산 경로가 몇 가지 인지 구하는 프로그램을 작성하세요.

▣ 입력설명

첫 번째 줄에 N(5<=N<=13)주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.

▣ 출력설명

등산경로의 가지수를 출력한다.

▣ 입력예제 

5
2 23 92 78 93 
59 50 48 90 80 
30 53 70 75 96 
94 91 82 89 93 
97 98 95 96 100

▣ 출력예제 

5

'''

import sys
from collections import deque

count = 0

def findMinMax(input_list):
    minValue = 10000000
    maxValue = 0

    minXY = (0,0)
    maxXY = (0,0)

    for i in range(len(input_list)):
        for j in range(len(input_list)):
            tmp = input_list[i][j]

            if tmp < minValue:
                minValue = tmp
                minXY = (i,j)
            
            if tmp > maxValue:
                maxValue = tmp
                maxXY = (i,j)

    return minXY, maxXY

def dfs(start, end, input_list):
    global count
    x = start[0]
    y = start[1]

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    if x == end[0] and y == end[1]:
        count += 1
        return
    else:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x > -1 and new_y > -1 and new_x < len(input_list) and new_y < len(input_list):
                if input_list[x][y] < input_list[new_x][new_y]:
                    dfs((new_x,new_y),end,input_list)

    pass

def logic(input_file_path, output_file_path):
    global count
    sys.stdin = open(input_file_path, "rt")

    result = 0 

    N = int(input())

    input_list = [list(map(int,input().split())) for _ in range(N)]

    start, end = findMinMax(input_list)

    dfs(start, end,input_list)
    
    result = count

    count = 0

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
