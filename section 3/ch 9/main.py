'''

클래스 명 : Ch 9

설명 : 봉우리 알고리즘 풀기 입니다.

작성일 : 2022.03.29

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

지도 정보가 N*N 격자판에 주어집니다. 
각 격자에는 그 지역의 높이가 쓰여있습니다. 
각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 
봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

▣ 입력설명

첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.

▣ 출력설명

봉우리의 개수를 출력하세요.

▣ 입력예제 

5
53723 
37161 
72534 
43641 
87352
    

▣ 출력예제 

10

'''

import sys

def check(input_list, tmp_list, N):
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if input_list[i][j] > input_list[i][j-1] and input_list[i][j] > input_list[i][j+1] and input_list[i][j] > input_list[i-1][j] and input_list[i][j] > input_list[i+1][j]:
                count += 1
    return count
    
def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    N = int(input())

    input_list = []
    input_list.append([0 for _ in range(N+2)])
    for i in range(N):
        tmp = list(map(int,input().split()))
        tmp.insert(0, 0)
        tmp.append(0)
        input_list.append(tmp)
    input_list.append([0 for _ in range(N+2)])

    tmp_list = [[0 for _ in range(N+2)] for _ in range(N+2)]

    result = check(input_list, tmp_list, N)

    sys.stdin = open(output_file_path, "rt")

    answer = int(input())

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
