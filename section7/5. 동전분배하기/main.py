'''

클래스 명 : Ch 5

설명 : 동전 분배하기 입니다.

작성일 : 2022.05.23

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다.
세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 
총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
단 세 사람의 총액은 서로 달라야 합니다.

▣ 입력설명

첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다. 
그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.

▣ 출력설명

총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.

▣ 입력예제 

7
8
9
11 
12 
23 
15 
17

▣ 출력예제 

5

'''


import sys

m = 1000000

def dfs(i, a, b, c, input_list):

    global m

    if i == len(input_list):
        if a==b or b==c or a==c:
            return

        tmp = max(a,b,c) - min(a,b,c)

        if m > tmp:
            m=tmp
    else:
        dfs(i+1,a+input_list[i],b,c,input_list)
        dfs(i+1,a,b+input_list[i],c,input_list)
        dfs(i+1,a,b,c+input_list[i],input_list)
    '''
    
    '''
    
def logic(input_file_path, output_file_path):
    global m
    sys.stdin = open(input_file_path, "rt")
    result = 0

    N = int(input())

    input_list = [int(input()) for _ in range(N)]

    dfs(0,0,0,0,input_list)

    result = m

    m = 1000000

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
