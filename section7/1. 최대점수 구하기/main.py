'''

클래스 명 : Ch 11

설명 : 최대 점수 구하기 입니다.

작성일 : 2022.05.23

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

이번 정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 풀려고 합니다. 
각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩 니다. 
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다. 
(해당문제는 해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다.)

▣ 입력설명

첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.

▣ 출력설명

첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.

▣ 입력예제 

5 20
10 5
25 12
15 8 
6 3 
7 4

▣ 출력예제 

41

'''


import sys

tmp = 0

def dfs(i,s_point,s_time,m,input_list):
    global tmp

    if s_time <= m:
        if s_point > tmp:
            tmp = s_point

    if i == len(input_list):
        return
    else:
        dfs(i+1,s_point+input_list[i][0],s_time+input_list[i][1],m,input_list)
        dfs(i+1,s_point,s_time,m,input_list)

def logic(input_file_path, output_file_path):
    global tmp
    sys.stdin = open(input_file_path, "rt")
    result = 0

    N, M = map(int,input().split())

    input_list = [list(map(int,input().split())) for _ in range(N)]

    dfs(0,0,0,M,input_list)

    result = tmp
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
