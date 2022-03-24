'''

클래스 명 : Ch 2

설명 : 숫자만 추출 알고리즘 풀기 입니다.

작성일 : 2022.03.24

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다. 
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉 첫자리 0은 자연수화 할 때 무시합니다. 출력은 120을 출력하고, 다음 줄에 120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

▣ 입력설명

첫 줄에 숫자가 섞인 문자열이 주어집니다. 
문자열의 길이는 50을 넘지 않습니다.

▣ 출력설명

첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.

▣ 입력예제 

g0en2Ts8eSoft

▣ 출력예제 

28
6

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    M = input()

    result = ""
    for i in range(len(M)):
        if ord(M[i]) > 47 and ord(M[i]) < 58:
            result = result + M[i]
    
    count = 0
    for i in range(1, int(result)+1):
        if int(result) % i == 0:
            count += 1
    
    sys.stdin = open(output_file_path, "rt")
    answer_1 = int(input())
    answer_2 = int(input())

    print(f"{input_file_path} 숫자 : {int(result) == answer_1}")
    print(f"{input_file_path} 약수 수 : {count == answer_2}")




if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
