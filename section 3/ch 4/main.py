'''

클래스 명 : Ch 4

설명 : 두 리스트 합치기 알고리즘 풀기 입니다.

작성일 : 2022.03.26

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.

▣ 입력설명

첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명

오름차순으로 정렬된 리스트를 출력합니다.

▣ 입력예제 

3
135
5
23679

▣ 출력예제 

12335679

'''

import sys

def sort(M):

    for i in range(len(M)):
        for j in range(i, len(M)):
            tmp = 0
            if M[i] > M[j]:
                tmp = M[i]
                M[i] = M[j]
                M[j] = tmp
    
    return M

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    com_list = []

    for i in range(2):
        N = int(input())
        M = list(map(int, input().split()))
        com_list = com_list + M
    
    #result = sort(com_list)
    com_list.sort(reverse=False)
    
    sys.stdin = open(output_file_path, "rt")

    answer = list(map(int,input().split()))

    #print(f"{input_file_path} : {result == answer}")
    print(f"{input_file_path} : {com_list == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
