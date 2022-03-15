'''

클래스 명 : Ch 6

설명 : 자릿수의 합 알고리즘 풀기 입니다.

작성일 : 2022.03.16

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

▣ 입력설명

첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 
각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명

자릿수의 합이 최대인 자연수를 출력한다. 
자릿수의 합이 같을 경우 입력순으로 먼저인 숫자 를 출력합니다.

▣ 입력예제 

3
125 15232 97

▣ 출력예제 

97

fix >


'''

import sys

def digit_sum(x):
    tmp = 0
    for i in x:
        tmp = tmp + int(i)
    return tmp

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N = int(input())

    input_list = input().split()

    result_list = []
    for i, v in enumerate(input_list):
        result_list.append((i, v, digit_sum(v)))

    result_list.sort(key = lambda x:(-x[2],x[0]))

    result = result_list[0][1]

    sys.stdin = open(output_file_path, "rt")

    answer = input()

    print(f"{input_file_path} : {result == answer}")
    

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
