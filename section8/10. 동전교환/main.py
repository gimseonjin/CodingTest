'''

클래스 명 : Ch 10

설명 : 동전교환 입니다.

작성일 : 2022.06.06

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환 해주려면 어떻게 주면 되는가? 
각 단위의 동전은 무한정 쓸 수 있다.

▣ 입력설명

첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 
두 번째 줄에는 N개의 동전의 종 류가 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다.
각 동전의 종류는 100원을 넘지 않는다.

▣ 출력설명

첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.

▣ 입력예제 

3
1 2 5
15


▣ 출력예제 

3

'''

import sys
from collections import deque


def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N = int(input())

    input_list = list(map(int, input().split()))

    M = int(input())
    
    count_list = [0 for i in range(M+1)]

    for i in input_list:
        for j in range(i, M+1):
            tmp = count_list[j]
            if tmp > count_list[j%i] + j // i or tmp == 0:
                count_list[j] = count_list[j%i] + j // i
                
    result = count_list[M]

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 2):
        logic(f"in{i}.txt", f"out{i}.txt")