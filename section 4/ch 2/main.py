'''

클래스 명 : Ch 2

설명 : 랜선자르기 알고리즘 풀기 입니다.

작성일 : 2022.04.28

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 
그러나 K개의 랜선은 길이가 제각각이다. 
선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정하자. 
N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.


예제설명) 802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다.

▣ 입력설명

첫째 줄에는 엘리트학원이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. 
K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 
그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의   이하의 자연수로 주어진다.

▣ 출력설명

첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.


▣ 입력예제 

4 11
802
743
457 
539

▣ 출력예제 

200

'''

import sys

def check(l, input_list):
    result = 0
    for i in input_list:
        result = result + i // l
    return result

def search(M, lt, rt, input_list, tmp):
    mid = (lt + rt) // 2

    result = check(mid, input_list)

    if lt > rt :
        return mid

    if result >= M :
        return search(M, mid + 1, rt, input_list, mid)

    if result < M :
        return search(M, lt, mid - 1, input_list, tmp)

    
def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")

    N, M = map(int,input().split())
    input_list = []

    for _ in range(N):
        input_list.append(int(input()))
    
    input_list.sort(reverse=True)

    result = search(M,1,input_list[0],input_list,0)

    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")

if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")