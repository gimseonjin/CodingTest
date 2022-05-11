'''

클래스 명 : Ch 6

설명 : 씨름 선수 알고리즘 풀기 입니다.

작성일 : 2022.04.28

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습 니다. 현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
“다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자 만 뽑기로 했습니다.”
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니다.

▣ 입력설명

첫째 줄에 지원자의 수 N(5<=N<=50)이 주어집니다.
두 번째 줄부터 N명의 키와 몸무게 정보가 차례로 주어집니다. 각 선수의 키와 몸무게는 모두 다릅니다.

▣ 출력설명

첫째 줄에 씨름 선수로 뽑히는 최대 인원을 출력하세요.

▣ 입력예제 

5
172 67
183 65
180 70 
170 72 
181 60

▣ 출력예제 

3

(183, 65), (180, 70), (170, 72)가 선발됩니다. 
(181, 60)은 (183, 65) 때문에 탈락하고, (172, 67)은 (180, 70) 때문에 탈락합니다.

'''

import sys

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N = int(input())

    input_list = [list(map(int, input().split())) for _ in range(N)]
    
    input_list.sort(key= lambda x :(x[1], x[0]))

    result = 0

    for i in range(len(input_list)):
        target = input_list[i]
        for j in range(i, len(input_list)):
            if target[0] < input_list[j][0] and target[1] < input_list[j][1]:
                break
        else:
            result += 1
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
