'''

클래스 명 : Ch 6

설명 : 알파 코드 입니다.

작성일 : 2022.05.25

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 

철수와 영희는 서로의 비밀편지를 암호화해서 서로 주고받기로 했다. 그래서 서로 어떻게 암 호화를 할 것인지 의논을 하고 있다.
영희 : 우리 알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당하여 번호로 보내기 로 하자.
철수 : 정말 바보같은 생각이군!! 생각해 봐!! 만약 내가 “BEAN"을 너에게 보낸다면 그것을 암 호화하면 25114이잖아!! 
그러면 이것을 다시 알파벳으로 복원할 때는 많은 방법이 존재하는 데 어떻게 할건데... 
이것을 알파벳으로 바꾸면 BEAAD, YAAD, YAN, YKD 그리고 BEKD로 BEAN말고도 5가지나 더 있군.
당신은 위와 같은 영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데 얼마나 많은 방법인 있는지 구하세요.

▣ 입력설명

첫 번째 줄에 숫자로 암호화된 코드가 입력된다. 
(코드는 0으로 시작하지는 않는다, 코드의 길 이는 최대 50이다) 
0이 입력되면 입력종료를 의미한다.

▣ 출력설명

입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력한다. 
그 가지 수도 출력한다. 단어의 출력은 사전순으로 출력한다.

▣ 입력예제 

25114

▣ 출력예제 

BEAAD
BEAN
BEKD
YAAD 
YAN 
YKD 
6

'''


import sys

count = 0

def dfs(i,s,input_list,password):
    global count
    if i == len(input_list):
        count += 1
        return
    else:
        if int(input_list[i]) != 0:
            dfs(i+1,s+password[int(input_list[i])],input_list,password)
        else :
            return
        if int(input_list[i:i+2]) < 26 and i+2 < len(input_list)+1:
            dfs(i+2,s+password[int(input_list[i:i+2])],input_list,password)
    pass
    
def logic(input_file_path, output_file_path):
    global count
    sys.stdin = open(input_file_path, "rt")
    result = 0

    password = ["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    words = input()
    
    dfs(0,"",words,password)

    result = count
    count = 0
    print(result)

    sys.stdin = open(output_file_path, "rt")
    
    #answer = int(input())

    #print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
