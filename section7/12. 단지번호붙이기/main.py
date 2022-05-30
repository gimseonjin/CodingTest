'''

클래스 명 : Ch 12

설명 : 단지 번호 붙이기 입니다.

작성일 : 2022.05.31

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
그림1과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸 다.
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한 다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
그림2는 그림1을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지 에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

▣ 입력설명

첫 번째줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력 되고 그 다음 N줄에는 각각 N개의 자료(0 혹은 1)가 입력된다.

▣ 출력설명

첫 번째줄에는 총 단지수를 출력하시오. 그리고 각 단지내의 집의 수를 오름차순으로 정렬하 여 한줄에 하나씩 출력하시오

▣ 입력예제 

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

▣ 출력예제 

3 
7 
8 
9

'''

import sys
from collections import deque

def findEstates(input_list):

    l = len(input_list)
    result = []

    for i in range(l):
        for j in range(l):
            find_house = findHouse(i,j,input_list)

            if find_house != 0:
                result.append(find_house)

    result.sort()
    return result

def findHouse(x, y, input_list):

    def is_visited(q : deque, tmp, input_list):
        q.append(tmp)
        input_list[tmp[0]][tmp[1]] = 0

    if input_list[x][y] != 1:
        return 0
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    is_visited(q,(x,y),input_list)
    
    count = 1
    while q:
        tmp = q.popleft()

        for i in range(4):
            new_x = tmp[0] + dx[i]
            new_y = tmp[1] + dy[i]

            if new_x > -1 and new_x < len(input_list) and new_y > -1 and new_y < len(input_list):
                if input_list[new_x][new_y] == 1:
                    is_visited(q,(new_x,new_y),input_list)
                    count += 1
    
    return count


def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N = int(input())

    input_list = [list(map(int,list(input()))) for _ in range(N)]
    
    result = findEstates(input_list)

    print(len(result))

    for i in result:
        print(i)

    print("=========="*2)

    sys.stdin = open(output_file_path, "rt")
    
    #answer = int(input())

    #print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")