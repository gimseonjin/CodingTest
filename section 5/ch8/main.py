'''

클래스 명 : Ch 8

설명 : 단어 찾기 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
현수는 영어로 시는 쓰는 것을 좋아합니다.
현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다. 
여러분이 찾아 주세요.

▣ 입력설명

첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 
이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.

▣ 출력설명

첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.

▣ 입력예제 
5
big
good
sky 
blue 
mouse 
sky 
good 
mouse 
big

▣ 출력예제 
blue

'''

'''
1. N 개의 입력값을 input_queue에 담습니다.
2. N-1개의 입력값을 use_list에 담습니다.
3. input_queue를 탐색하면서 use_list에 있는 지 체크합니다.
4. use_list에 없으면 result에 담습니다.
'''
import sys
from collections import deque

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    N = int(input())
    
    input_queue = deque([input() for _ in range(N)])
    use_list = [input() for _ in range(N-1)]

    while input_queue:
        tmp = input_queue.popleft()

        if tmp not in use_list:
            result = tmp
            break


    sys.stdin = open(output_file_path, "rt")
    
    answer = input()

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
