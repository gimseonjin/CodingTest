'''

클래스 명 : Ch 9

설명 : 수열 추측하기 입니다.

작성일 : 2022.05.20

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다. 그리고 둘째 줄부터 차례대로 파스칼 의 삼각형처럼 위의 두개를 더한 값이 저장되게 된다. 
예를 들어 N이 4 이고 가장 윗 줄에 3 1 2 4 가 있다고 했을 때, 다음과 같은 삼각형이 그려진다.
3124 
436 
79 
16
N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램을 작성하 시오. 
단, 답이 여러가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력하여야 한다.

▣ 입력설명

첫째 줄에 두개의 정수 N(1≤N≤10)과 F가 주어진다. 
N은 가장 윗줄에 있는 숫자의 개수를 의 미하며 F는 가장 밑에 줄에 있는 수로 1,000,000 이하이다.

▣ 출력설명

첫째 줄에 삼각형에서 가장 위에 들어갈 N개의 숫자를 빈 칸을 사이에 두고 출력한다. 
답이 존재 하지 않는 경우는 입력으로 주어지지 않는다.

▣ 입력예제 

4 16

▣ 출력예제 

3124

'''


import sys
from collections import deque
from itertools import permutations

def do(t_list):
    tmp_list = []
    for i in range(len(t_list)-1):
        x = t_list[i]
        y = t_list[i+1]
        tmp_list.append(x+y)
    return tmp_list

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = 0

    N, M = map(int, input().split())
    
    input_list = [i for i  in range(1,N+1)]

    tmp_list = permutations(input_list, N)
    
    for t in tmp_list:
        tmp = t
        while len(tmp) > 1:
            tmp = do(tmp)
        if tmp[0] == M:
            result = list(t)
            break
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = list(map(int, input().split()))

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
