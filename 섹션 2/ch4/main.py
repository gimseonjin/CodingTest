'''

클래스 명 : Ch 4

설명 : 대표값 알고리즘 풀기 입니다.

작성일 : 2022.03.15

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

N명의 학생의 수학점수가 주어집니다. 
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높 은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

▣ 입력설명

첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다. 
학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명

첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 
평균은 소수 첫째 자리에서 반올림합니다.

▣ 입력예제 

10 
45 73 66 87 92 67 75 79 75 80

▣ 출력예제 

74 7

fix >

round 함수는 round_half_even 방식이다.

round_half_even 방식은 xx.5일 때, 짝수 쪽으로 가버린다.

즉 65.5 는 66.0, 64.5는 64.0, 으로 간다.

따라서 다음과 같이 수정한다.

avg = int(sum(input_list) / len(input_list) + 0.5)

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N = int(input())

    input_list = list(map(int,input().split()))

    avg = int(sum(input_list) / len(input_list) + 0.5)

    result_list = []

    for i, v in enumerate(input_list):
        result = (v, abs(avg - v), i+1)
        result_list.append(result)

    result_list.sort(key = lambda x:(x[1],-x[0],x[2]))

    result = f"{avg} {result_list[0][2]}"

    sys.stdin = open(output_file_path, "rt")

    answer = input()

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
