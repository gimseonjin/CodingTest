'''

클래스 명 : Ch 6

설명 : 응급실 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
메디컬 병원 응급실에는 의사가 한 명밖에 없습니다.
응급실은 환자가 도착한 순서대로 진료를 합니다. 하지만 위험도가 높은 환자는 빨리 응급조치를 의사가 해야 합니다. 
이런 문제를 보완하기 위해 응급실은 다음과 같은 방법으로 환자의 진료순서를 정합니다.
• 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
• 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로
다시 넣습니다. 그렇지 않으면 진료를 받습니다.
현재 N명의 환자가 대기목록에 있습니다.
N명의 대기목록 순서의 환자 위험도가 주어지면, 대기목록상의 M번째 환자는 몇 번째로 진료 를 받는지 출력하는 프로그램을 작성하세요.
대기목록상의 M번째는 대기목록의 제일 처음 환자를 0번째로 간주하여 표현한 것입니다.

▣ 입력설명

첫 줄에 자연수 N(5<=N<=100)과 M(0<=M<N) 주어집니다.
두 번째 줄에 접수한 순서대로 환자의 위험도(50<=위험도<=100)가 주어집니다.
위험도는 값이 높을 수록 더 위험하다는 뜻입니다. 같은 값의 위험도가 존재할 수 있습니다.

▣ 출력설명

M번째 환자의 몇 번째로 진료받는지 출력하세요.

▣ 입력예제 
5 2
60 50 70 80 90

▣ 출력예제 
3

▣ 입력예제 2
60
60 60 90 60 60 60

▣ 출력예제 2 
5

'''

'''
1. 입력 받은 대기 인원을 list로 받는다.
2. 여기서 위험도 순서대로 정렬된 list와 index를 붙인 정렬되지 않은 queue를 준비한다.
3. 만약 list[last]와 queue.popleft가 같으면 진료를 한다.
4. 진료를 하면 list.pop()을 수행한다.
5. 진료를 하지 않으면 다시 queue에 넣는다.
6. index와 M 값이 같으면 출력한다.
'''
import sys
from collections import deque

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    N, M = map(int,input().split())
    input_list = list(map(int,input().split()))

    q = deque([ [i, v] for i, v in enumerate(input_list)])
    sort_list = input_list
    sort_list.sort()

    count = 0
    while q :
        tmp = q.popleft()
        if sort_list[len(sort_list)-1] == tmp[1]:
            count += 1
            sort_list.pop()
            if tmp[0] == M:
                result = count
                break
        else :
            q.append(tmp)
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
