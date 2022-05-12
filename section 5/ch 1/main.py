'''

클래스 명 : Ch 1 

설명 : 가장 큰 수 알고리즘 풀기 입니다.

작성일 : 2022.05.12

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하 여 가장 큰 수를 만들라고 했습니다. 
여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
7823이 가장 큰 숫자가 됩니다.

▣ 입력설명

첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.

▣ 출력설명

가장 큰 수를 출력합니다.

▣ 입력예제 

5276823 3

▣ 출력예제 

7823

'''

import sys
from typing import Set

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    input_list, N = input().split()

    input_list = list(input_list)

    count = int(N)

    i = 0

    while count > 0:

        tmp = input_list[i]

        if len(input_list) - i == count:
            input_list = input_list[:-count]
            break

        for j in range(i, count+i+1):
            if tmp < input_list[j]:
                input_list.pop(i)
                count -= 1
                break
        else:
            i += 1
        
    result = "".join(input_list)

    sys.stdin = open(output_file_path, "rt")
    
    answer = input()

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
