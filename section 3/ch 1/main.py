'''

클래스 명 : Ch 1 

설명 : 회문 문자열 검사 알고리즘 풀기 입니다.

작성일 : 2022.03.24

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

▣ 입력설명

첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 
각 단어의 길이는 100을 넘지 않는다.

▣ 출력설명

각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

▣ 입력예제 

5
level
moon
abcba 
soon 
gooG

▣ 출력예제 

#1 YES
#2 NO
#3 YES
#4 NO #5 YES

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N = int(input())

    result_list = []
    for i in range(N):
        message = str(input()).lower()

        result = "YES"
        for i in range(len(message)):
            if message[i] != message[len(message)-1 - i]:
                result = "NO"
                break
        
        result_list.append(result)
    
    sys.stdin = open(output_file_path, "rt")
    for i in range(N):
        answer = input()
        result = f"#{i+1} {result_list[i]}"
        print(f"{input_file_path} case{i+1}: {result == answer}")
    


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
