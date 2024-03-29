'''

클래스 명 : Ch 8

설명 : 곳감(모래시계) 알고리즘 풀기 입니다.

작성일 : 2022.03.29

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 
현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 
그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.
첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회 전하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.

▣ 입력설명

첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다. 
그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령 정보가 M줄에 걸쳐 주어집니다.

▣ 출력설명

총 감의 개수를 출력합니다.

▣ 입력예제 

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3 
2 0 3 
5 1 2 
3 1 4
    

▣ 출력예제 

379

'''

import sys

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    N = int(input())
    input_list = []
    for i in range(N):
        input_list.append(list(map(int,input().split())))

    M = int(input())  
    order_list = []
    for i in range(M):
        order_list.append(list(map(int,input().split())))

    for order in order_list:
        if order[1] == 1:
            for i in range(order[2]):
                input_list[order[0]-1].insert(0, input_list[order[0]-1].pop())
        else:
            for i in range(order[2]):
                input_list[order[0]-1].append(input_list[order[0]-1].pop(0))

    '''
    for order in order_list:
        if order[1] == 1:
            tmp = [0 for i in range(N)]
            for i, v in enumerate(input_list[order[0]-1]):
                tmp_i = i + order[2]
                if tmp_i >= N :
                    tmp_i = tmp_i - N
                tmp[tmp_i] = v
            input_list[order[0]-1] = tmp
        else:
            tmp = [0 for i in range(N)]
            for i, v in enumerate(input_list[order[0]-1]):
                tmp_i = i - order[2]
                if tmp_i < 0 :
                    tmp_i = tmp_i + N
                tmp[tmp_i] = v
            input_list[order[0]-1] = tmp
    '''
    half = int(N/2 + 0.5)

    result = 0
    for i in range(N):
        low = N-i-1
        col = i+1

        if i < half:
            low = i
            col = N-i
        result = result + sum(input_list[i][low:col])

    sys.stdin = open(output_file_path, "rt")

    answer = int(input())

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
