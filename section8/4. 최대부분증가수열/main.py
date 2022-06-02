'''

클래스 명 : Ch 2

설명 : 최대 부분 증가수열 입니다.

작성일 : 2022.06.02

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

N개의 자연수로 이루어진 수열이 주어졌을 때, 그 중에서 가장 길게 증가하는(작은 수에서 큰 수로) 원소들의 집합을 찾는 프로그램을 작성하라. 
예를 들어, 원소가 2, 7, 5, 8, 6, 4, 7, 12, 3 이면 가장 길게 증가하도록 원소들을 차례대로 뽑아내면 
2, 5, 6, 7, 12를 뽑아내어 길 이가 5인 최대 부분 증가수열을 만들 수 있다.

▣ 입력설명

첫째 줄은 입력되는 데이터의 수 N(2≤N≤1,000, 자연수)를 의미하고, 둘째 줄은 N개의 입력데이터들이 주어진다.

▣ 출력설명

첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.


▣ 입력예제 

8 
53786294

▣ 출력예제 

4

'''

import sys
from collections import deque


def dynamic(N, input_list, count_list):

    if count_list[N] != 0:
        return count_list[N]

    if N == 0:
        count_list[N] = 1
        return count_list[N]
    
    tmp = 0
    for i in range(N):
        count = 1
        if input_list[N] > input_list[i]:
            count += dynamic(i,input_list,count_list)
        if count > tmp:
            tmp = count
    
    count_list[N] = tmp
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