'''

클래스 명 : Ch 9

설명 : Anagram 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아 나그램이라고 합니다.
예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 즉 어느 한 단어를 재 배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세 요. 아나그램 판별시 대소문자가 구분됩니다.

▣ 입력설명

첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다. 
단어의 길이는 100을 넘지 않습니다.

▣ 출력설명

두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.

▣ 입력예제 
AbaAeCe 
baeeACA

▣ 출력예제 
YES

'''

'''
1. 두 입력값의 길이가 같다고 가정한다.
2. 두 입력값을 각각 deque에 넣는다.
3. 1번 입력값의 단어를 체크한다(중복값 제거).
4. 중복값 제거한 단어를 tmp에 담고 한 개씩 탐색한다.
5. tmp를 탐색하면서 각 deque에 몇 개씩 들어잇는 지 확인한다.
6. 갯수가 같으면 pass 틀리면 NO를 result에 넣는다.
7. tmp 탐색이 끝날 때까지 NO가 안나오면 result에 Yes를 담는다.
'''
import sys
from collections import deque

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    input1 = input()
    input2 = input()

    input1_que = deque(input1)
    input2_que = deque(input2)

    tmp = set(input1)

    for t in tmp:
        x = input1_que.count(t)
        y = input2_que.count(t)
        if x != y:
            result = "NO"
            break
    else:
        result = "YES"
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = input()

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
