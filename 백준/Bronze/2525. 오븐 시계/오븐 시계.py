hour, min = map(int,input().split()) # 현재 시간과 분을 입력받기
cook_time = int(input()) # 조리시간 입력받기

new_time = min + cook_time # 현재 시간에서 조리시간을 더한 값(분 단위)

if new_time >= 60: # 분 단위가 60분을 넘어가면
    hour += new_time // 60 # 총 조리시간에서 60으로 나눈 몫을 시간에 더하기
    min = new_time % 60 # 분은 총 조리시간에서 60으로 나눈 나머지 할당
    if hour > 23: # 근데 시간 값이 23을 넘어가면 (24시가 넘어버리면)
        hour -= 24 # 24시간을 빼주면서 0시 단위로 설정
    print(hour, min)
else:
    print(hour, new_time)