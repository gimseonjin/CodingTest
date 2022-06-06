'''

클래스 명 : Ch 7

설명 : 가방 입니다.

작성일 : 2022.06.06

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

최고 17kg의 무게를 저장할 수 있는 가방이 있다. 
그리고 각각 3kg, 4kg, 7kg, 8kg, 9kg의 무게를 가진 5종류의 보석이 있다. 
이 보석들의 가치는 각각 4, 5, 10, 11, 13이다.
이 보석을 가방에 담는데 17kg를 넘지 않으면서 최대의 가치가 되도록 하려면 어떻게 담아야 할까요? 
각 종류별 보석의 개수는 무한이 많다. 한 종류의 보석을 여러 번 가방에 담을 수 있 다는 뜻입니다.

▣ 입력설명

첫 번째 줄은 보석 종류의 개수와 가방에 담을 수 있는 무게의 한계값이 주어진다. 
두 번째 줄부터 각 보석의 무게와 가치가 주어진다.
가방의 저장무게는 1000kg을 넘지 않는다. 보석의 개수는 30개 이내이다.

▣ 출력설명

첫 번째 줄에 가방에 담을 수 있는 보석의 최대가치를 출력한다.


▣ 입력예제 

4 11
5 12
3 8
6 14 
4 8


▣ 출력예제 

25

'''

import sys
from collections import deque


def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N, M = map(int, input().split())

    input_list = [list(map(int, input().split())) for _ in range(N)]
    
    count_list = [0 for i in range(M+1)]

    for i in input_list:

        k = i[0]
        v = i[1]

        for j in range(k, M+1):
            tmp = count_list[j]
            if tmp < count_list[j-k] + v:
                count_list[j] = count_list[j-k] + v
        
    result = count_list[M]

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")