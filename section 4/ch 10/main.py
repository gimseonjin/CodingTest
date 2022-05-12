'''

클래스 명 : Ch 8

설명 : 침몰하는 타이타닉 알고리즘 풀기 입니다.

작성일 : 2022.05.12

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 1부터 n까지 각각의 수 앞 에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.
예를 들어 다음과 같은 수열의 경우 48625137
1앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5. 이렇게 5개이고,
2앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,
3앞에 놓인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개
따라서 48625137의 경우, 53402110이 된다.
n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원래의 수열을 출력하는 프로그램을 작성하세요.

▣ 입력설명

첫 번째 줄에 자연수 N(3<=N<100)이 주어지고, 
두 번째 줄에는 역수열이 숫자 사이에 한칸의 공백을두고 주어진다.

▣ 출력설명 
원래 수열을 출력합니다.

▣ 입력예제 1

8
5 3 4 0 2 1 1 0

▣ 출력예제 1

4 8 6 2 5 1 3 7

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N = int(input())
    
    input_list = list(map(int, input().split()))

    result = []

    for i in reversed(range(N)):

        result.insert(input_list[i], i+1)

    sys.stdin = open(output_file_path, "rt")
    
    answer = list(map(int, input().split()))

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
