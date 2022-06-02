'''

클래스 명 : Ch 1

설명 : 네트워크 선 자르기 입니다.

작성일 : 2022.06.01

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

현수는 네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다. 예를 들어 4m의 네트워크 선이 주어진다면

1) 1m+1m+1m+1m 
2) 2m+1m+1m
3) 1m+2m+1m
4) 1m+1m+2m
5) 2m+2m

의 5가지 방법을 생각할 수 있습니다. (2)와 (3)과 (4)의 경우 왼쪽을 기준으로 자르는 위치가 다르면 다른 경우로 생각한다.
그렇다면 네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?

▣ 입력설명

첫째 줄은 네트워크 선의 총 길이인 자연수 N(3≤N≤45)이 주어집니다.

▣ 출력설명

첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.


▣ 입력예제 

7

▣ 출력예제 

21

'''

import sys
from collections import deque


# 바텀 업
def dynamic(N, count_list):

    if count_list[N] != 0:
        return count_list[N]

    if N == 1:
        return 1

    if N == 2:
        return 2
    
    count_list[N] = dynamic(N-1, count_list) + dynamic(N-2, count_list)

    return count_list[N]

def dynamicWithFor(N, count_list):

    for i in range(1,N+1):
        if i == 1:
            count_list[i] = 1
        elif i == 2:
            count_list[i] = 2
        else :
            count_list[i] = count_list[i-1] + count_list[i-2]
    
    return count_list[N]



def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N = int(input())

    count_list = [0 for _ in range(N+1)]

    result = dynamic(N, count_list)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 2):
        logic(f"in{i}.txt", f"out{i}.txt")