'''

클래스 명 : Ch 7

설명 : 교육과정 설계 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
현수는 1년 과정의 수업계획을 짜야 합니다.
수업중에는 필수과목이 있습니다. 이 필수과목은 반드시 이수해야 하며, 그 순서도 정해져 있 습니다.
만약 총 과목이 A, B, C, D, E, F, G가 있고, 여기서 필수과목이 CBA로 주어지면 필수과목은 C, B, A과목이며 이 순서대로 꼭 수업계획을 짜야 합니다.
여기서 순서란 B과목은 C과목을 이수한 후에 들어야 하고, A과목은 C와 B를 이수한 후에 들 어야 한다는 것입니다.
현수가 C, B, D, A, G, E로 수업계획을 짜면 제대로 된 설계이지만
C, G, E, A, D, B 순서로 짰다면 잘 못 설계된 수업계획이 됩니다.
수업계획은 그 순서대로 앞에 수업이 이수되면 다음 수업을 시작하다는 것으로 해석합니다. 수업계획서상의 각 과목은 무조건 이수된다고 가정합니다.
필수과목순서가 주어지면 현수가 짠 N개의 수업설계가 잘된 것이면 “YES", 잘못된 것이면 ”NO“를 출력하는 프로그램을 작성하세요.

▣ 입력설명

첫 줄에 한 줄에 필수과목의 순서가 주어집니다. 모든 과목은 영문 대문자입니다.
두 번째 줄에 N(1<=N<=10)이 주어집니다.
세 번 째 줄부터 현수가 짠 N개의 수업설계가 주어집니다.(수업설계의 길이는 30이하이다) 
수업설계는 같은 과목을 여러 번 이수하도록 설계해도 됩니다.

▣ 출력설명

수업설계가 잘된 것이면 “YES", 잘못된 것이면 ”NO“를 출력합니다.

▣ 입력예제 
CBA
3
CBDAGE 
FGCDAB 
CTSBDEA

▣ 출력예제 
#1 YES
#2 NO
#3 YES

'''

'''
1. 필수 수강 과목을 list에 담는다.
2. 각 교육 과정 별로 왼쪽에서부터 탐색한다.
3. list[last]와 같으면 pop 한다.
4. 탐색 중, list 길이가 0이면 YES, 0이 아니면 NO를 출력한다.
'''
import sys
from collections import deque

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = []

    N = input()
    M = int(input())

    for _ in range(M):
        s_list = list(N[::-1])
        q = deque(list(input()))
        while q :
            tmp = q.popleft()
            if tmp == s_list[len(s_list)-1]:
                s_list.pop()
            if len(s_list) == 0:
                result.append("YES")
                break
        else:
            result.append("NO")
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = []
    for _ in range(M):
        answer.append(input().split(" ")[1])

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
