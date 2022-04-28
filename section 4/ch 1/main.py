'''

클래스 명 : Ch 1 

설명 : 이분검색 알고리즘 풀기 입니다.

작성일 : 2022.04.28

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
임의의 N개의 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요. 
단 중복값은 존재하지 않습니다.

▣ 입력설명

첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다. 
두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.

▣ 출력설명

첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.

▣ 입력예제 

8 32
23 87 65 12 57 32 99 81

▣ 출력예제 

3

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N, M = map(int,input().split())

    input_list = list(map(int, input().split()))

    input_list.append(M)

    input_list.sort()

    result = input_list.index(M)+1

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
