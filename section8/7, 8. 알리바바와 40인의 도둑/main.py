'''

클래스 명 : Ch 6

설명 : 가장 높은 탑 쌓기 입니다.

작성일 : 2022.06.03

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다.
알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다. 
계곡의 돌다리는 N×N개의 돌들로 구성되어 있다. 
각 돌다리들은 높이가 서로 다릅니다.
해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 
이동은 최단거리 이동을 합니다. 즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다.
N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의 최소량을 구하는 프로그램을 작성하세요.



▣ 입력설명

첫 번째 줄에는 자연수 N(1<=N<=20)이 주어진다.
두 번째 줄부터 계곡의 N*N 격자의 돌다리 높이(10보다 작은 자연수) 정보가 주어진다.


▣ 출력설명

첫 번째 줄에 (1, 1)출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.


▣ 입력예제 

5
37219 
58392 
53123 
54321 
17524

▣ 출력예제 

25

'''

import sys
from collections import deque


def dynamic(N, input_list, count_list):

    for i in range(1,N):
        for j in range(1,N):
            count_list[i][j] = min(count_list[i-1][j], count_list[i][j-1]) + input_list[i][j]

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N = int(input())

    input_list = [list(map(int, input().split())) for _ in range(N)]

    count_list = [[0 for _ in range(N)] for _ in range(N)]

    x_tmp = 0
    y_tmp = 0
    for i in range(N):
        x_tmp = x_tmp + input_list[0][i]
        y_tmp = y_tmp + input_list[i][0]
        count_list[0][i] = x_tmp
        count_list[i][0] = y_tmp

    dynamic(N, input_list, count_list)

    result = count_list[N-1][N-1]

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")