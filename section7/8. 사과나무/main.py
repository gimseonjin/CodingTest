'''

클래스 명 : Ch 8

설명 : 사과나무 입니다.

작성일 : 2022.05.26

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다. 
N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다.
현수과 수확하는 사과의 총 개수를 출력하세요.

▣ 입력설명

첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 
이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다. 
각 격자안의 사과의 개수는 100을 넘지 않는다.

▣ 출력설명

수확한 사과의 총 개수를 출력합니다.

▣ 입력예제 

5
10 13 10 12 15 
12 39 30 23 11 
11 25 50 53 15 
19 27 29 37 27 
19 13 30 13 19

▣ 출력예제 

379

'''

import sys
from collections import deque

def bfs(N, input_list):
    h = N // 2
    q = deque([(h,h)])
    visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
    xDot = [0,0,1,-1]
    yDot = [1,-1,0,-0]
    s = 0
    while q:
        tmp = q.popleft()

        if tmp[0] == -1 or tmp[0] == N or tmp[1] == -1 or tmp[1] == N:
            break

        else:

            if visited[tmp[0]][tmp[1]] == 0:
                s += input_list[tmp[0]][tmp[1]]
                visited[tmp[0]][tmp[1]] = 1

            for i in range(4):
                x = tmp[0] + xDot[i]
                y = tmp[1] + yDot[i]
                if visited[x][y] == 0:
                    q.append((x ,y))
            
    return s


def logic(input_file_path, output_file_path):
    sys.stdin = open(input_file_path, "rt")

    result = 0

    N = int(input())

    input_list = [list(map(int,input().split())) for _ in range(N)]

    result = bfs(N,input_list)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
