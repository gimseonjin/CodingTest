'''

클래스 명 : Ch 5

설명 : 공주님 구하기 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
정보 왕국의 이웃 나라 외동딸 공주가 숲속의 괴물에게 잡혀갔습니다.
정보 왕국에는 왕자가 N명이 있는데 서로 공주를 구하러 가겠다고 합니다. 정보왕국의 왕은 다음과 같은 방법으로 공주를 구하러 갈 왕자를 결정하기로 했습니다.
왕은 왕자들을 나이 순으로 1번부터 N번까지 차례로 번호를 매긴다. 그리고 1번 왕자부터 N 번 왕자까지 순서대로 시계 방향으로 돌아가며 동그랗게 앉게 한다. 그리고 1번 왕자부터 시 계방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다. 한 왕자가 K(특정숫자)를 외치면 그 왕자는 공주를 구하러 가는데서 제외되고 원 밖으로 나오게 된다. 그리고 다음 왕자부터 다시 1부터 시작하여 번호를 외친다.
이렇게 해서 마지막까지 남은 왕자가 공주를 구하러 갈 수 있다.

예를 들어 총 8명의 왕자가 있고, 3을 외친 왕자가 제외된다고 하자. 처음에는 3번 왕자가 3 을 외쳐 제외된다. 이어 6, 1, 5, 2, 8, 4번 왕자가 차례대로 제외되고 마지막까지 남게 된 7 번 왕자에게 공주를 구하러갑니다.
N과 K가 주어질 때 공주를 구하러 갈 왕자의 번호를 출력하는 프로그램을 작성하시오.

▣ 입력설명

첫 줄에 자연수 N(5<=N<=1,000)과 K(2<=K<=9)가 주어진다.

▣ 출력설명

첫 줄에 마지막 남은 왕자의 번호를 출력합니다.

▣ 입력예제 

8 3

▣ 출력예제 

7

'''

'''
1. 1 ~ N 까지의 숫자를 가진 Queue를 준비한다.
2. popleft를 통해 앞에서 부터 숫자를 가져온다.
3. count를 통해 M인 경우, 가져온 숫자를 버리고 count를 0으로 초기화 한다.
4. count가 M이 아닌 경우, 다시 Queue에 넣는다.
5. queue가 0일 때, 가져온 숫자를 result에 넣는다.
'''
import sys
from collections import deque

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    N, M = map(int,input().split())

    q = deque([ str(_ + 1) for _ in range(N)])
    
    count = 0
    
    while True:
        count += 1
        tmp = q.popleft()

        if len(q) == 0:
            result = int(tmp)
            break

        if count == M:
            count = 0
        else:
            q.append(tmp)
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
