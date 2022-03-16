'''

클래스 명 : Ch 6

설명 : 뒤집은 소수 알고리즘 풀기 입니다.

작성일 : 2022.03.16

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 
예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다. 
단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하 여 프로그래밍 한다.

▣ 입력설명

첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 
각 자연수의 크기는 100,000를 넘지 않는다.

▣ 출력설명

첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

▣ 입력예제 

5
32 55 62 3700 250

▣ 출력예제 

23 73

fix >


'''

import sys

def reverse(x):
    return int(x[::-1])

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x/2)):
        if x % i == 0:
            return False
    
    return True

def logic(input_file_path, output_file_path):

    sys.stdin = open(input_file_path, "rt")

    N = int(input())

    input_list = input().split()

    result = ""
    for i in input_list:
        rev = reverse(i)
        if isPrime(rev):
            result = result + str(rev) + " "

    sys.stdin = open(output_file_path, "rt")

    answer = input()

    print(f"{input_file_path} : {result[:-1] == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
