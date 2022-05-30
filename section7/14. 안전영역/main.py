'''

클래스 명 : Ch 14

설명 : 안전 영역 입니다.

작성일 : 2022.05.31

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다. 
먼저 어떤 지역의 높이 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 때 
물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다. 
이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다.

▣ 입력설명

첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. 
N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N 개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N 개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

▣ 출력설명

첫째 줄에 장마철에 물에 잠기지 않는 안전한영역의 최대 개수를 출력한다.

▣ 입력예제 

5
68262 
32346 
67332 
72536 
89527

▣ 출력예제 

5

'''

import sys
from collections import deque

def findPlace(x,y,h,input_list, tmp_list):
    
    if tmp_list[x][y] == 1 :
        return False

    if input_list[x][y] < h :
        return False
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    tmp_list[x][y] = 1
    q.append((x,y))

    while q:
        tmp = q.popleft()

        for i in range(4):
            new_x = tmp[0] + dx[i]
            new_y = tmp[1] + dy[i]

            if new_x > -1 and new_x < len(input_list) and new_y > -1 and new_y < len(input_list):
                if input_list[new_x][new_y] >= h and tmp_list[new_x][new_y] != 1 :
                    tmp_list[new_x][new_y] = 1
                    q.append((new_x, new_y))
            
    return True

def findAllPlace(h,input_list):
    l = len(input_list)
    tmp_list=[[0]*l for _ in range(l)]

    count = 0

    for i in range(l):
        for j in range(l):
            if findPlace(i,j,h,input_list,tmp_list):
                count += 1
    return count

def searchSafePlace(input_list):
    count = 0

    for i in range(100):

        tmp = findAllPlace(i+1,input_list)


        if tmp > count:
            count = tmp

    return count


def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N = int(input())

    input_list = [list(map(int,input().split())) for _ in range(N)]
    
    result = searchSafePlace(input_list)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")

