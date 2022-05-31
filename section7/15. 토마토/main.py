'''

클래스 명 : Ch 15

설명 : 토마토 입니다.

작성일 : 2022.06.01

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
현수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
토마토는 아래의 그림 과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 
아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 
익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향 에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토 가 혼자 저절로 익는 경우는 없다고 가정한다. 
현수는 창고에 보관된 토마토들이 며칠이 지나 면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들 의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로 그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

▣ 입력설명

첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다. M은 상자의 가로 칸의 수, N 은 상자의 세로 칸의 수를 나타낸다. 
단, 2 ≤ M, N ≤ 1,000 이다.
둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
즉, 둘째 줄부터 N개의 줄 에는 상자에 담긴 토마토의 정보가 주어진다. 
하나의 줄에는 상자 가로줄에 들어있는 토마토 의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

▣ 출력설명

여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

▣ 입력예제 

6 4 
0 0 -1 0 0 0 
0 0 1 0 -1 0 
0 0 -1 0 0 0
0 0 0 0 -1 1

▣ 출력예제 

4

'''

import sys
from collections import deque

def findList(input_list,N,M,k):
    find_list = []

    for i in range(M):
        for j in range(N):
            if input_list[i][j] == k:
                find_list.append((i,j))

    return find_list

def spreadTomato(input_list, one_list, N, M):

    tmp_list = [[0 for _ in range(N)] for _ in range(M)]

    q = deque(one_list)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    max = 0
    while q:
        tmp = q.popleft()

        for i in range(4):
            new_x = tmp[0] + dx[i]
            new_y = tmp[1] + dy[i]

            if new_x > -1 and new_x < M and new_y > -1 and new_y < N:
                if input_list[new_x][new_y] == 0:
                    input_list[new_x][new_y] = 1
                    tmp_list[new_x][new_y] = tmp_list[tmp[0]][tmp[1]] + 1
                    if tmp_list[new_x][new_y] > max:
                        max = tmp_list[new_x][new_y]
                    q.append((new_x, new_y))
    return max

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N, M = map(int, input().split())

    input_list = [list(map(int,input().split())) for _ in range(M)]
    
    one_list = findList(input_list,N,M,1)
    count = spreadTomato(input_list,one_list,N,M)
    zero_list = findList(input_list,N,M,0)

    if len(zero_list) == 0 :
        result = count
    else:
        result = -1
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
