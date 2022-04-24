'''

클래스 명 : Ch 11

설명 : 격자판 회문수 알고리즘 풀기 입니다.

작성일 : 2022.04.24

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요. 
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
구부러진 경우(87178)는 회문수로 간주하지 않습니다.

▣ 입력설명

1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.

▣ 출력설명

5자리 회문수의 개수를 출력합니다.

▣ 입력예제 

2415326 
3518717 
8327138 
6123211 
1313532 
1125652 
1222215
    

▣ 출력예제 

3

'''

import sys
    
def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    input_list = [list(map(int, input().split())) for _ in range(7)]

    result = 0

    for i in range(7):
        for j in range(7):
            if( j > 1 and j < 5
                and
                input_list[i][j-1] == input_list[i][j+1]
                and
                input_list[i][j-2] == input_list[i][j+2]):
                result = result + 1

            if( i > 1 and i < 5
                and
                input_list[i-1][j] == input_list[i+1][j]
                and
                input_list[i-2][j] == input_list[i+2][j]):
                result = result + 1

    sys.stdin = open(output_file_path, "rt")

    answer = int(input())

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
