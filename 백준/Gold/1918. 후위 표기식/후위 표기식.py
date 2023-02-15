char = list(map(str, input())) # 문자열 입력받기

# 스택 밖에 있을때 연산자의 우선순위 (in coming priority)
icp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 3}
# 스택 밖에 있을때 연산자의 우선순위 (in stack priority)
isp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}

stack = [] # 연산자 잠시 담아놓을 stack
res = '' # 후위연산자 결과를 담을 문자열


for c in char:
    if 65 <= ord(c) <= 90: # 알파벳 대문자이면
        res += c # res 에 붙이기
    else: # 연산자면
        if c == ')': # 닫는 연산자인지 확인
            while stack and stack[-1] != '(': # 스택이 비어있지 않고 top 에 있는 원소가 ( 일 때까지
                res += stack.pop() # 뽑아서 계속 추가
            stack.pop() # 여는 연산자가 나오면 while 문이 끝날테니까 여는 괄호 날려버리기
        else: # 닫는 괄호가 아니라 기타연산자
            # 현재 연산자의 우선순위보다 스택의 top 에 있는 연산자의 우선순위가 같거나 높으면 계속 pop
            while stack and isp[stack[-1]] >= icp[c]:
                res += stack.pop()

            # 그게 아니면 스택에 연산자 추가
            stack.append(c)


while stack:
    res += stack.pop()

print(res)