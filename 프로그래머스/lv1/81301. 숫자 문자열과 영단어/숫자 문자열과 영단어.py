def solution(s):
    word_match = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    answer = ''
    tmp = ''

    for i in s:
        if i.isdigit(): # 숫자면
            answer += i # 바로 추가
        else: # 문자면
            tmp += i # 하나의 문자열이 될때까지 누적
            for key in word_match:
                if key in tmp:
                    answer +=  word_match[key]
                    tmp = ''
    
    return int(answer)