'''

클래스 명 : Ch 10

설명 : 스도쿠 알고리즘 풀기 입니다.

작성일 : 2022.04.24

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9 개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 예를 들어 다음을 보자.

위 그림은 스도쿠를 정확하게 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오 고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색 깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.

▣ 입력설명

첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.

▣ 출력설명

첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

▣ 입력예제 

143628579 
572139468 
986754231 
391542786 
468917352 
725863914 
237481695 
619275843 
854396127
    

▣ 출력예제 

YES

'''

import sys
    
def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    input_list = [list(map(int, input().split())) for _ in range(9)]

    result = "YES"

    for i in range(9):
        if(len(set(input_list[i])) != 9):
            result = "NO"

    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(input_list[i][j])
        if(len(set(temp)) != 9):
            result = "NO"

    for i in range(0,9,3):
        for j in range(0,9,3):
            temp = []
            for k in range(3):
                for k2 in range(3):
                    temp.append(input_list[i+k][j+k2])
            if len(set(temp)) != 9:
                result = "NO"

    sys.stdin = open(output_file_path, "rt")

    answer = input()

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
