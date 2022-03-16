'''

클래스 명 : Ch 6

설명 : 소수(에라토스테네스 체) 알고리즘 풀기 입니다.

작성일 : 2022.03.16

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 제한시간은 1초입니다.

▣ 입력설명

첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

▣ 출력설명

첫 줄에 소수의 개수를 출력합니다.

▣ 입력예제 

20

▣ 출력예제 

8

fix >

output.txt 파일들의 encoding이 일치하지 않는다.

1,2,5 = utf-8
3,4 = utf-16

3,4를 utf-8로 수정해야한다.

'''

import sys

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    N = int(input())
    
    input_list = [0 for i in range(N+1)]

    result = 0

    for i in range(2, N+1):
        if input_list[i] == 0:
            result += 1
            for j in range(i, N+1, i):
                input_list[j] = 1
    
    print(result)

    #sys.stdin = open(output_file_path, "rt", encoding = "utf-16")

    #answer = int(input())

    #print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
