'''

클래스 명 : Ch 2

설명 : 부분집합 구하기(DFS) 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 을 작성하세요.

▣ 입력설명

첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.

▣ 출력설명

첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력예제와 같은 순서로 출력한다. 
단 공집합은 출력하지 않습니다.

▣ 입력예제 
3

▣ 출력예제 
123
12
13
1 
23
2
3

'''

'''

핵심 : 
-> 자기 포함 출력 한번
-> 자기 제외 출력 한번

1. N을 입력받는다.
2. { i : 출력 유무 }의 dict를 만든다.
3. 자기 포함 출력 한 번, 자기 제외 출력 한 번, 총 두번을 출력한다.
'''

import sys

def do(i, input_list):
    if i == len(input_list) :
        for j in range(i):
            if input_list[j][j] == True:
                print(j+1, end = " ")
        print()
    else:
        input_list[i][i] = True
        do(i+1, input_list)
        input_list[i][i] = False
        do(i+1, input_list)

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    N = int(input())
    input_list = [{v : False} for v in range(N)]

    result = do(0, input_list)
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = input()

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 2):
        logic(f"in{i}.txt", f"out{i}.txt")
