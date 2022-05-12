'''

클래스 명 : Ch 8

설명 : 침몰하는 타이타닉 알고리즘 풀기 입니다.

작성일 : 2022.05.12

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열 을 만듭니다. 
이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니 다.
예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4, 왼쪽끝에서5를가져와 2345증가수열을만들수있습니다.

▣ 입력설명

첫째 줄에 자연수 N(3<=N<=100)이 주어집니다. 
두 번째 줄에 N개로 구성된 수열이 주어집니다.

▣ 출력설명

첫째 줄에 최대 증가수열의 길이를 출력합니다.
두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 ‘L', 오른쪽 끝에서 가져갔으면 ’R'를 써 간 문자열을 출력합니다.
(단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)

▣ 입력예제 1

5
2 4 5 1 3

▣ 출력예제 1

4
L R L L 

▣ 입력예제 2

10
3 2 10 1 5 4 7 8 9 6

▣ 출력예제 2

3
L R R

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N = int(input())
    
    input_list = list(map(int, input().split()))

    result = ""

    i = 0
    tmp = 0

    while i < N:
        check_list = []
        check_list.append([input_list[0], "L"])
        check_list.append([input_list[len(input_list) - 1], "R"])
        check_list.sort(key = lambda x : x[0])

        if check_list[0][0] > tmp:
            tmp = check_list[0][0]
            result += check_list[0][1]

            if check_list[0][1] == "L":
                input_list = input_list[1:]
            else:
                input_list.pop()


        elif check_list[1][0] > tmp:
            tmp = check_list[1][0]
            result += check_list[1][1]

            if check_list[1][1] == "L":
                input_list = input_list[1:]
            else:
                input_list.pop()
        
        else:
            break

        i += 1
        
    sys.stdin = open(output_file_path, "rt")
    
    answer_i = int(input())
    answer_result = input()

    print(f"{input_file_path} : {i == answer_i and result == answer_result}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
