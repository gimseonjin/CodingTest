'''

클래스 명 : Ch 5

설명 : 최대 선 연결하기 입니다.

작성일 : 2022.06.03

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

왼쪽의 번호와 오른쪽의 번호가 있는 그림에서 같은 번호끼리 선으로 연결하려고 합니다. 
왼쪽번호는 무조건 위에서부터 차례로 1부터 N까지 오름차순으로 나열되어 있습니다.
 오른쪽의 번호 정보가 위부터 아래 순서로 주어지만 서로 선이 겹치지 않고 최대 몇 개의 선 을 연결할 수 있는 지 구하는 프로그램을 작성하세요.
위의 그림은 오른쪽 번호 정보가 4 1 2 3 9 7 5 6 10 8 로 입력되었을 때 선이 서로 겹치지 않고 연결할 수 있는 최대 선을 개수 6을 구한 경우입니다.

▣ 입력설명

첫 줄에 자연수 N(1<=N<=100)이 주어집니다.
두 번째 줄에 1부터 N까지의 자연수 N개의 오른쪽 번호 정보가 주어집니다. 
순서는 위쪽번호 부터 아래쪽번호 순으로입니다.

▣ 출력설명

첫 줄에 겹치지 않고 그을 수 있는 최대선의 개수를 출력합니다.


▣ 입력예제 

10
4 1 2 3 9 7 5 6 10 8

▣ 출력예제 

6

'''

import sys
from collections import deque


def dynamic(N, input_list, count_list):

    if count_list[N] != 0:
        return count_list[N]
    
    if N == 0:
        count_list[N] = 1
        return count_list[N]
    else:
        count = 1
        for i in range(N):
            if input_list[i] < input_list[N]:
                tmp = dynamic(i,input_list,count_list) + 1
                if count < tmp:
                    count = tmp
        count_list[N] = count
        return count_list[N]


def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N = int(input())

    input_list = list(map(int, input().split()))

    count_list = [0 for _ in range(N)]

    for i in range(N):
        dynamic(i, input_list, count_list)
        if result < max(count_list):
            result = max(count_list)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")