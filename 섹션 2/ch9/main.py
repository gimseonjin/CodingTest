'''

클래스 명 : Ch 9

설명 : 주사위 게임 알고리즘 풀기 입니다.

작성일 : 2022.03.16

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된 다. 
또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다. 
3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금 으로 받게 된다.

N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램 을 작성하시오

▣ 입력설명

첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 
그 다음 줄부터 N개의 줄에 사람 들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

▣ 출력설명

첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.

▣ 입력예제 

3
3 3 6 
2 2 2 
6 2 5


▣ 출력예제 

12000

fix >


'''

import sys


def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    N = int(input())

    result = 0

    for i in range(N):
        input_list = list(map(int,input().split()))
        
        case = set(input_list)

        tmp = 0

        if len(case) == 1:
            tmp = 10000 + list(case)[0] * 1000
        if len(case) == 2:
            tmp = 1000 + max(input_list, key = input_list.count) * 100
        if len(case) == 3:
            input_list.sort(reverse = True)
            tmp = input_list[0] * 100
        
        if result < tmp :
            result = tmp

    sys.stdin = open(output_file_path, "rt")

    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
