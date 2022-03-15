'''

클래스 명 : Ch 2

설명 : K번째 큰 수 알고리즘 풀기 입니다.

작성일 : 2022.03.15

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 
같은 숫자의 카드가 여러장 있을 수 있습니다. 
현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려 고 합니다. 
3장을 뽑을 수 있는 모든 경우를 기록합니다. 
기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.

▣ 입력설명

첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 된다.

▣ 출력설명

첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.

▣ 입력예제 

10 3
13 15 34 23 45 65 33 11 26 42

▣ 출력예제 

143

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N, K = map(int, input().split())

    input_list = list(map(int, input().split()))

    result_list = set()

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                result_list.add(input_list[i] + input_list[j] + input_list[k])
    
    result_list = list(result_list)

    result_list.sort(reverse=True)

    result = result_list[K-1]

    sys.stdin = open(output_file_path, "rt")

    answer = int(input())

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
