'''

클래스 명 : Ch 9

설명 : 미로의 최단거리 입니다.

작성일 : 2022.05.30

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
7*7 격자판 미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요. 
출발점은 격 자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 
격자판의 1은 벽이고, 0은 통로이다. 격 자판의 움직임은 상하좌우로만 움직인다. 

▣ 입력설명

7*7 격자판의 정보가 주어집니다.

▣ 출력설명

첫 번째 줄에 경로의 가지수를 출력한다.

▣ 입력예제 

0000000 
0111110 
0001000 
1101011 
1100001 
1101100 
1000000

▣ 출력예제 

8

'''

import sys
from collections import deque

count = 0

def dfs(x, y, input_list):

    global count 
    
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    if x < 0 or y < 0 or x > len(input_list)-1 or y > len(input_list)-1:
        return

    if input_list[x][y] == 1:
        return

    if x == 6 and y == 6:
        count += 1
        return
    else:
        for i in range(4):
            input_list[x][y] = 1
            dfs(x+dx[i], y+dy[i], input_list)
            input_list[x][y] = 0


def logic(input_file_path, output_file_path):
    global count
    sys.stdin = open(input_file_path, "rt")

    result = 0

    input_list = [list(map(int,input().split())) for _ in range(7)]

    dfs(0,0,input_list)
    
    result = count

    count = 0

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
