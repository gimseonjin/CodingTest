'''

클래스 명 : Ch 5

설명 : 정다면체 알고리즘 풀기 입니다.

작성일 : 2022.03.16

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

▣ 입력설명

첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

▣ 출력설명

첫 번째 줄에 답을 출력합니다.

▣ 입력예제 

4 6

▣ 출력예제 

5 6 7

fix >


'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N, M = map(int, input().split())

    result_list = [0 for i in range(N+M+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            result_list[i+j] = result_list[i+j] + 1

    max_value = max(result_list)
    result = ""
    for i, v in enumerate(result_list):
        if v == max_value:
            result = result + str(i) + " "

    sys.stdin = open(output_file_path, "rt")
    answer = input()

    print(f"{input_file_path} : {result[:-1] == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
