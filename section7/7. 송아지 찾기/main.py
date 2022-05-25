'''

클래스 명 : Ch 7

설명 : 송아지 찾기 입니다.

작성일 : 2022.05.26

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 
현수의 위치와 송아 지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.
현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다. 
최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성 하세요.

▣ 입력설명

첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000 까지이다.

▣ 출력설명

점프의 최소횟수를 구한다.

▣ 입력예제 

5 14

▣ 출력예제 

3

'''

import sys
from collections import deque

def bfs(f,t):
    q = deque()
    is_visited = [0] * (10000+1)
    q.append(f)
    while q:
        tmp = q.popleft()
        if tmp == t:
            break
        else :
            for i in (tmp-1,tmp+1,tmp+5):
                if 0<= i <= 10000:
                    if is_visited[i] == 0:
                        q.append(i)
                        is_visited[i] = is_visited[tmp]+1

    return is_visited[t]


def logic(input_file_path, output_file_path):
    sys.stdin = open(input_file_path, "rt")

    result = 0

    N, M= map(int, input().split())

    result = bfs(N,M)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
