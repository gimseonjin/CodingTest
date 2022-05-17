'''

클래스 명 : Ch 4

설명 : 후위식 연산 입니다.

작성일 : 2022.05.17

수정자 : 김선진

수정한 날자 : 0000.00.00

Todo > 
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.

▣ 입력설명

첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다. 
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.

▣ 출력설명

연산한 결과를 출력합니다.


▣ 입력예제 

352+*9-

▣ 출력예제 

12

'''

'''
1. 후위 연산식을 가져온다.
2. 앞에서부터 순차적으로 탐색하며 stack에 넣는다.
3. 기호 탐색 시 pop() 두번해서 값을 가져온 후, 계산해서 다시 넣는다.
4. 마지막까지 탐색이 끝나면 stack에 담겨있는 값을 가져온다.
'''
import sys

def cal(x,y,c):
    if c == "+":
        return str(int(x)+int(y))
    elif c == "-":
        return str(int(x)-int(y))
    elif c == "/":
        return str(int(x)/int(y))
    else :
        return str(int(x)*int(y))

def logic(input_file_path, output_file_path):
    
    sys.stdin = open(input_file_path, "rt")
    result = ""

    N = input()
    stack = []

    for n in N:
        if n.isdecimal():
            stack.append(n)
        else :
            y = stack.pop()
            x = stack.pop()
            stack.append(cal(x,y,n))

    result = int(stack[0])
    
    sys.stdin = open(output_file_path, "rt")
    
    answer = int(input())

    print(f"{input_file_path} : {result == answer}")


if __name__ == "__main__":
    for i in range(1, 6):
        logic(f"in{i}.txt", f"out{i}.txt")
