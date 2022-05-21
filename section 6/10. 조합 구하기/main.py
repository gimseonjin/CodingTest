'''

클래스 명 : Ch 10

설명 : 조합 구하기 입니다.

작성일 : 2022.05.21

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
1부터N까지번호가적힌구슬이있습니다.이중 M개를뽑는방법의수를출력하는프로그 램을 작성하세요.


▣ 입력설명

첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명

첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 출력순서는 사전순으로 오름차순으로 출력합니다.

▣ 입력예제 

4 2

▣ 출력예제 

12
13
14
23 
24 
34 
6

'''


import sys
from collections import deque
from itertools import combinations

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = 0

    N, M = map(int, input().split())
    
    input_list = [i for i  in range(1,N+1)]

    tmp_list = list(combinations(input_list, M))
    
    for t in tmp_list:
        print(t[0], t[1])
    
    print(len(tmp_list))
    
    sys.stdin = open(output_file_path, "rt")
    
    #answer = list(map(int, input().split()))

    #print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 2):
        logic(f"in{i}.txt", f"out{i}.txt")
