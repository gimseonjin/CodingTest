'''

클래스 명 : Ch 5

설명 : 중복순열 구하기 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다. 각 섬은 1로 표시되어 상하좌우와 대 각선으로 연결되어 있으며, 0은 바다입니다. 
섬나라 아일랜드에 몇 개의 섬이 있는지 구하는 프로그램을 작성하세요.

▣ 입력설명

첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다. 
두 번째 줄부터 격자판 정보가 주어진다.

▣ 출력설명

첫 번째 줄에 섬의 개수를 출력한다.

▣ 입력예제 

7 
1100010 
0110110 
0100000 
0001011 
1101100 
1000100 
1010100

▣ 출력예제 
5

'''

'''

-> DFS의 핵심, 자기 포함, 미포함으로 전체 N 까지 들어가서 한 개씩 계산해나온다!!

핵심 : 
-> 자기 포함 출력 한번
-> 자기 제외 출력 한번

1. N을 입력받는다.
2. { n : 출력 유무 }의 dict를 만든다.
3. 자기 포함 출력 한 번, 자기 제외 출력 한 번, 총 두번을 출력한다.



1. M ㅊㅔ크 후, M보다 작으면 출력 후, 다음 Death
2. M이랑 같으면 print() -> return
'''

import sys
from collections import deque

def bfs(row, cal, input_list):
    dx = [1,0,-1,0,-1,1,-1,1]
    dy = [0,-1,0,1,-1,-1,1,1]

    q = deque([[row,cal]])
    input_list[row][cal] = 0
    while q:
        tmp = q.popleft()
        for i in range(8):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0<=x<=len(input_list) -1 and 0<=y<=len(input_list) -1 and input_list[x][y] == 1:
                input_list[x][y] = 0
                q.append([x,y])


def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = 0

    N = int(input())

    input_list = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if input_list[i][j] == 1:
                bfs(i,j,input_list)
                result += 1

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
