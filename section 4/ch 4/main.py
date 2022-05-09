'''

클래스 명 : Ch 4

설명 : 마굿간 알고리즘 풀기 입니다.

작성일 : 2022.04.28

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

▣ 입력설명

첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다. 
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.

▣ 출력설명

첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.

▣ 입력예제 

5 3
1
2
8 
4 
9

▣ 출력예제 

3

'''

import sys

def checkList(input_list, M):
    
    count = 1
    tmp = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] - tmp >= M:
            count += 1
            tmp = input_list[i]
    
    return count
    

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N, M = map(int, input().split())

    input_list = [int(input()) for _ in range(N)]
    input_list.sort()

    lt = 1
    rt = max(input_list)

    result = 0
    while lt <= rt:

        mid = (lt + rt) // 2
        count = checkList(input_list, mid)

        if count >= M:
            result = mid
            lt = mid + 1
        else:
            rt = mid - 1

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
