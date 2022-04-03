'''

클래스 명 : Ch 5

설명 : 수들의 합 알고리즘 풀기 입니다.

작성일 : 2022.03.26

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

▣ 입력설명

첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 
다음 줄에는 A[1], A[2], ..., A[N]이 공백으로 분리되어 주어진다. 
각각의 A[x]는 30,000을 넘지 않는 자연수이다.

▣ 출력설명

첫째 줄에 경우의 수를 출력한다.

▣ 입력예제 

8 3 
1 2 1 3 1 1 1 2

▣ 출력예제 

5

'''

import sys

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    N, M = map(int, input().split())

    input_list = list(map(int, input().split()))

    result = 0

    for i in range(0, N):
        for j in range(i, N):
            if M < sum(input_list[i:j+1]):
                break
            if M == sum(input_list[i:j+1]):
                result += 1
                break

    sys.stdin = open(output_file_path, "rt")

    answer = int(input())


    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
