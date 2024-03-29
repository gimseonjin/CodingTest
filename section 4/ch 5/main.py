'''

클래스 명 : Ch 5

설명 : 회의실 배정 알고리즘 풀기 입니다.

작성일 : 2022.04.28

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들 려고 한다. 
각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 
단, 회의는 한번 시작하면 중간에 중 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

▣ 입력설명

첫째 줄에 회의의 수 n(1<=n<=100,000)이 주어진다. 
둘째 줄부터 n+1 줄까지 각 회의의 정 보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.

▣ 출력설명

첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라.

▣ 입력예제 

5
1 4
2 3
3 5 
4 6 
5 7

▣ 출력예제 

3

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N = int(input())

    input_list = [list(map(int, input().split())) for _ in range(N)]
    
    input_list.sort(key= lambda x :(x[1], x[0]))

    result = 0
    tmp = 0

    for x,y in input_list:
        if x >= tmp:
            result += 1
            tmp = y

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
