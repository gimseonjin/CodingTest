'''

클래스 명 : Ch 1

설명 : 재귀함수를 이용한 이진수 출력 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 
단 재귀함수를 이용 해서 출력해야 합니다.

▣ 입력설명

첫 번째 줄에 10진수 N(1<=N<=1,000)이 주어집니다.

▣ 출력설명

첫 번째 줄에 이진수를 출력하세요.

▣ 입력예제 
11

▣ 출력예제 
1011

'''

'''
1. N을 입력받는다.
2. N을 2로 나눈 나머지를 더하는 함수를 구한다.
2. N을 2로 나눴을 때, 0이 아니면 자신을 다시 호출한다.
'''

import sys

def do(N):
    if N // 2 == 0:
        return "1"
    else:
        return do(N // 2) + str(N % 2)

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    N = int(input())

    result = do(N)
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = input()

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
