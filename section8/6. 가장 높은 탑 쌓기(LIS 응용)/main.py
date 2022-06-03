'''

클래스 명 : Ch 6

설명 : 가장 높은 탑 쌓기 입니다.

작성일 : 2022.06.03

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 한다. 
탑은 벽돌을 한 개씩 아래 에서 위로 쌓으면서 만들어 간다. 
아래의 조건을 만족하면서 가장 높은 탑을 쌓을 수 있는 프 로그램을 작성하시오.

(조건1) 벽돌은 회전시킬 수 없다. 즉, 옆면을 밑면으로 사용할 수 없다.
(조건2) 밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다. 
(조건3) 벽돌들의 높이는 같을 수도 있다.
(조건4) 탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다. 
(조건5) 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.


▣ 입력설명

입력 파일의 첫째 줄에는 입력될 벽돌의 수가 주어진다. 
입력으로 주어지는 벽돌의 수는 최대 100개이다. 
둘째 줄부터는 각 줄에 한 개의 벽돌에 관한 정보인 벽돌 밑면의 넓이, 벽돌의 높 이 그리고 무게가 차례대로 양의 정수로 주어진다. 
각 벽돌은 입력되는 순서대로 1부터연속적 인 번호를 가진다.

▣ 출력설명

첫 번째 줄에 가장 높이 쌓을 수 있는 탑의 높이를 출력한다.


▣ 입력예제 

5
25 3 4
4 4 6
9 2 3 
16 2 5 
1 5 2


▣ 출력예제 

6

'''

import sys
from collections import deque


def dynamic(N, input_list, count_list):

    width = 0
    height = 1
    weight = 2

    if count_list[N] != 0:
        return count_list[N]

    if N == 0:
        count_list[N] = input_list[N][height]
        return count_list[N]
    
    count = input_list[N][height]
    for i in range(N):
        if input_list[N][width] < input_list[i][width] and input_list[N][weight] < input_list[i][weight]:
            tmp = input_list[N][height] + dynamic(i, input_list, count_list)
            if tmp > count:
                count = tmp
    count_list[N] = count
    return count_list[N]

    pass

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    result = 0

    N = int(input())

    input_list = [list(map(int, input().split())) for _ in range(N)]

    count_list = [0 for _ in range(N)]

    input_list.sort(key= lambda x : (x[0], x[2]), reverse= True)

    for i in range(N):
        tmp = dynamic(i, input_list, count_list)
        if tmp > result:
            result = tmp

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")