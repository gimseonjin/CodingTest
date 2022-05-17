'''

클래스 명 : Ch 3

설명 : 합이 같은 부분집합 구하기(DFS) 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고, 그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.
둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어 합니다.
예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이 16으로 같은 경우가 존재하는 것을 알 수 있다.

▣ 입력설명

첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
두 번째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.

▣ 출력설명

첫 번째 줄에 “YES" 또는 ”NO"를 출력한다.

▣ 입력예제 

6
1 3 5 6 7 10

▣ 출력예제 

YES

'''

'''

def DFS(L, sum):
    if sum>total//2:
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

-> DFS의 핵심, 자기 포함, 미포함으로 전체 N 까지 들어가서 한 개씩 계산해나온다!!

핵심 : 
-> 자기 포함 출력 한번
-> 자기 제외 출력 한번

1. N을 입력받는다.
2. { n : 출력 유무 }의 dict를 만든다.
3. 자기 포함 출력 한 번, 자기 제외 출력 한 번, 총 두번을 출력한다.
'''

import sys

def do(i, input_list, s):
    if s > sum(input_list) // 2:
        return

    if i == len(input_list):
        if s == (sum(input_list) - s):
            print("YES")
        return

    do(i+1, input_list, s + input_list[i])
    do(i+1, input_list, s)

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    N = int(input())
    input_list = list(map(int, input().split()))

    do(0, input_list, 0)
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = input()

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
