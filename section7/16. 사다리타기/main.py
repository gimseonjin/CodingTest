'''

클래스 명 : Ch 16

설명 : 사다리 타기 입니다.

작성일 : 2022.06.01

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

현수와 친구들은 과자를 사먹기 위해 사다리 타기를 합니다. 
사다리 표현은 2차원 평면은 0으 로 채워지고, 사다리는 1로 표현합니다. 
현수는 특정도착지점으로 도착하기 위해서는 몇 번째 열에서 출발해야 하는지 알고싶습니다. 
특정 도착지점은 2로 표기됩니다. 여러분이 도와주세 요. 

▣ 입력설명

10*10의 사다리 지도가 주어집니다.

▣ 출력설명

출발지 열 번호를 출력하세요.

▣ 입력예제 

1010010101 
1011110101 
1010010101 
1010010111 
1010010101 
1011110101 
1010010111 
1110010101 
1010011101 
1010020101

▣ 출력예제 

7

'''

import sys
from collections import deque

def checkBoard(input_list):

    for i in range(10):
        tmp_list = [[0 for _ in range(10)] for _ in range(10)]
        if findResult(i,0,input_list,tmp_list) :
            return i

def findResult(x,y,input_list,tmp_list):
    if input_list[y][x] == 0:
        return False
    if y == 9:
        if input_list[y][x] == 2:
            return True
        else:
            return False
    else:
        if x+1 < 10 and input_list[y][x+1] == 1 and tmp_list[y][x+1] == 0:
            tmp_list[y][x+1] = 1
            return findResult(x+1,y,input_list,tmp_list)

        elif x-1 > -1 and input_list[y][x-1] == 1 and tmp_list[y][x-1] == 0:
            tmp_list[y][x-1] = 1
            return findResult(x-1,y,input_list,tmp_list)

        else:
            tmp_list[y+1][x] = 1
            return findResult(x,y+1,input_list,tmp_list)


def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    input_list = [list(map(int,input().split())) for _ in range(10)]
    
    result = checkBoard(input_list)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")