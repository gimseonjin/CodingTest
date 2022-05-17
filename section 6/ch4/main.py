'''

클래스 명 : Ch 4

설명 : 바둑이 승차 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태 울수가 없다. 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.

▣ 입력설명

첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다. 
둘째 줄부터 N마리 바둑이의 무게가 주어진다.

▣ 출력설명

첫 번째 줄에 가장 무거운 무게를 출력한다.

▣ 입력예제 

259 5
81
58
42 
33 
61

▣ 출력예제 

242

'''

'''

-> DFS의 핵심, 자기 포함, 미포함으로 전체 N 까지 들어가서 한 개씩 계산해나온다!!

핵심 : 
-> 자기 포함 출력 한번
-> 자기 제외 출력 한번

1. N을 입력받는다.
2. { n : 출력 유무 }의 dict를 만든다.
3. 자기 포함 출력 한 번, 자기 제외 출력 한 번, 총 두번을 출력한다.
'''

import sys

def do(i, input_list, s):
    if s > input_list[len(input_list)-1]:
        return 0
    if i == len(input_list)-1:
        return s
    else:
        x = do(i+1, input_list, s)
        y = do(i+1, input_list, s+input_list[i])
        return x if x > y else y

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    N , M= map(int, input().split())
    
    input_list = [int(input()) for _ in range(M)]
    input_list.append(N)

    sys.stdin = open(output_file_path, "rt")
    
    answer = input()
    print(do(0, input_list, 0))

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(5, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
