'''

클래스 명 : Ch 2

설명 : K번째 수 알고리즘 풀기 입니다.

작성일 : 2022.03.15

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

▣ 입력설명

첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다. 
두 번째 줄에 N개의 숫자가 차례로 주어진다.

▣ 출력설명

각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.

▣ 입력예제 

2
6 2 5 3 
5 2 7 3 8 9 
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15

▣ 출력예제 

#1 7
#2 6

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    t = int(input())

    result_list = []

    for i in range(t):

        n, s, e, k = map(int, input().split())

        a = list(map(int,input().split()))

        result = a[s-1:e]

        result.sort()

        result_list.append(f"#{i+1} {result[k-1]}")


    sys.stdin = open(output_file_path, "rt")

    for i in range(t):
        answer = input()
        print(result_list[i] == answer)


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
