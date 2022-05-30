'''

클래스 명 : Ch 9

설명 : 미로의 최단거리 입니다.

작성일 : 2022.05.30

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력하는 프로그램을 작성하세요. 
경로수는 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다. 출발점은 격자의 (1, 1) 좌표이고, 탈 출 도착점은 (7, 7)좌표이다. 
격자판의 1은 벽이고, 0은 도로이다.
격자판의 움직임은 상하좌우로만 움직인다. 

▣ 입력설명

7*7 격자판의 정보가 주어집니다.

▣ 출력설명

첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.

▣ 입력예제 

0000000 
0111110 
0001000 
1101011 
1101000 
1000100 
1010000

▣ 출력예제 

12

'''

import sys
from collections import deque

def bfs(x, y, input_list):

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    q = deque([(x,y)])
    is_visited = []

    try:
        while True:
            tmp = q.popleft();
        
            if (6,6) in is_visited:
                return input_list[6][6]

            for i in range(4):

                new_x = tmp[0]+dx[i]
                new_y = tmp[1]+dy[i]

                if new_x > -1 and new_y > -1 and new_x < 7 and new_y < 7:
                    if input_list[new_x][new_y] == 0:
                        input_list[new_x][new_y] = input_list[tmp[0]][tmp[1]] + 1
                        is_visited.append((new_x,new_y))
                        q.append((new_x,new_y))
                        
    except IndexError:
        return -1



def logic(input_file_path, output_file_path):
    sys.stdin = open(input_file_path, "rt")

    result = 0

    input_list = [list(map(int,input().split())) for _ in range(7)]

    result = bfs(0,0,input_list)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
