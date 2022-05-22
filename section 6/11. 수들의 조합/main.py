'''

클래스 명 : Ch 11

설명 : 수들의 조합 입니다.

작성일 : 2022.05.22

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수 는 몇 개가 있는지 출력하는 프로그램을 작성하세요.
예를 들면 5개의 숫자 2 4 5 8 12가 주어지고, 3개를 뽑은 조합의 합이 6의 배수인 조합을 찾으면 4+8+12 2+4+12로 2가지가 있습니다.


▣ 입력설명

첫줄에 정수의 개수 N(3<=N<=20)과 임의의 정수 K(2<=K<=N)가 주어지고, 두 번째 줄에는 N개의 정수가 주어진다.
세 번째 줄에 M이 주어집니다.

▣ 출력설명

총 가지수를 출력합니다.

▣ 입력예제 

5 3
2 4 5 8 12
6

▣ 출력예제 

2

'''


import sys
from collections import deque
from itertools import combinations

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = 0

    N, K = map(int,input().split())

    input_list = list(map(int,input().split()))

    M = int(input())

    tmp_list = list(combinations(input_list,K))

    count = 0
    for tmp in tmp_list:
        if sum(tmp) % M == 0:
            count += 1

    result = count
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
