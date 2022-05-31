'''

클래스 명 : Ch 17

설명 : 피자 배달 거리 입니다.

작성일 : 2022.06.01

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

N×N 크기의 도시지도가 있습니다. 도시지도는 1×1크기의 격자칸으로 이루어져 있습니다. 
각 격자칸에는 0은 빈칸, 1은 집, 2는 피자집으로 표현됩니다. 
각 격자칸은 좌표(행번호, 열 번호) 로 표현됩니다. 행번호는 1번부터 N번까지이고, 열 번호도 1부터 N까지입니다.
도시에는 각 집마다 “피자배달거리”가 았는데 각 집의 피자배달거리는 해당 집과 도시의 존재 하는 피자집들과의 거리 중 최소값을 해당 집의 “피자배달거리”라고 한다.
집과 피자집의 피자배달거리는 |x1-x2|+|y1-y2| 이다. 예를 들어, 도시의 지도가 아래와 같다면

(1, 2)에 있는 집과 (2, 3)에 있는 피자집과의 피자 배달 거리는 |1-2| + |2-3| = 2가 된다. 최근 도시가 불경기에 접어들어 우후죽순 생겼던 피자집들이 파산하고 있습니다. 도시 시장은 도시에 있는 피자집 중 M개만 살리고 나머지는 보조금을 주고 폐업시키려고 합니다.
시장은 살리고자 하는 피자집 M개를 선택하는 기준으로 도시의 피자배달거리가 최소가 되는 M개의 피자집을 선택하려고 합니다.
도시의 피자 배달 거리는 각 집들의 피자 배달 거리를 합한 것을 말합니다.

▣ 입력설명

첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 12)이 주어진다. 
둘째 줄부터 도시 정보가 입력된다.

▣ 출력설명

첫째 줄에 M개의 피자집이 선택되었을 때 도시의 최소 피자배달거리를 출력한다.

▣ 입력예제 

4 4
0120 
1021 
0212 
2012

▣ 출력예제 

6

'''

import sys
from collections import deque
from itertools import combinations

def getLength(f, t):    
    return abs(f[0] - t[0]) + abs(f[1] - t[1])

def findList(input_list, what):
    what_list = []

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == what:
                what_list.append((i,j))
    
    return what_list

def totalLength(pizza_list, house_list):
    result = 0
    for h in house_list:
        s = 1000000
        for p in pizza_list:
            s = min(s, getLength(p,h))
        result += s
    return result

def getShortPizzaLength(last_pizza_list, house_list):
    result = 1000000
    for l in last_pizza_list:
        result = min(result,totalLength(l,house_list))
    return result

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N, M = map(int,input().split())

    input_list = [list(map(int,input().split())) for _ in range(N)]
    
    pizza_list = findList(input_list, 2)
    house_list = findList(input_list, 1)

    last_pizza_list = list(combinations(pizza_list, M))

    result = getShortPizzaLength(last_pizza_list, house_list)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
