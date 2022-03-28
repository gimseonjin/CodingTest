'''

클래스 명 : Ch 6

설명 : 격자판 최대합 알고리즘 풀기 입니다.

작성일 : 2022.03.29

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.

N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.

▣ 입력설명

첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.

▣ 출력설명

최대합을 출력합니다.

▣ 입력예제 

5
10 13 10 12 15 
12 39 30 23 11 
11 25 50 53 15 
19 27 29 37 27 
19 13 30 13 19

▣ 출력예제 

155

'''

import sys

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    N = int(input())
    input_list = []
    for i in range(N):
        input_list.append(list(map(int,input().split())))

    result = 0

    temp = []
    for i in range(N):
        temp.append(input_list[i][i])
    
    if result < sum(temp):
        result = sum(temp)
    
    temp = []
    for i in range(N):
        temp.append(input_list[N-1-i][i])
    
    if result < sum(temp):
        result = sum(temp)

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(input_list[i][j])
    
        if result < sum(temp):
            result = sum(temp)

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(input_list[j][i])
    
        if result < sum(temp):
            result = sum(temp)

    sys.stdin = open(output_file_path, "rt")

    answer = int(input())

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
