'''

클래스 명 : Ch 5

설명 : 중복순열 구하기 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력합니다.

▣ 입력설명

첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명

첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 
출력순서는 사전순으로 오름차순으로 출력합니다.

▣ 입력예제 

3 2

▣ 출력예제 
1 1
1 2
1 3
2 1 
2 2 
2 3 
3 1 
3 2 
3 3 
9

'''

'''

-> DFS의 핵심, 자기 포함, 미포함으로 전체 N 까지 들어가서 한 개씩 계산해나온다!!

핵심 : 
-> 자기 포함 출력 한번
-> 자기 제외 출력 한번

1. N을 입력받는다.
2. { n : 출력 유무 }의 dict를 만든다.
3. 자기 포함 출력 한 번, 자기 제외 출력 한 번, 총 두번을 출력한다.



1. M ㅊㅔ크 후, M보다 작으면 출력 후, 다음 Death
2. M이랑 같으면 print() -> return
'''

import sys

def do(r_list, i, j, k):
    if i == j:
        for _ in range(j):
            print(r_list[_], end = "")
        print()
    else:
        for _ in range(k):
            r_list[i] = _ + 1
            do(r_list, i+1, j, k)

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""
    N, M = map(int, input().split())
    r_list = [ 1 for _ in range(N)]

    do(r_list,0,M,N)

    sys.stdin = open(output_file_path, "rt")
    
    answer = input()

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(5, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
