x, y, w, h = map(int, input().split()) 
#현재 x좌표, y좌표, 전체 x좌표, y좌표
diff_lst = []

# 전체 좌표에서 현재 좌표까지의 차를 모두 구해서 list에 넣기
diff_lst.append(w-x)
diff_lst.append(x-0)
diff_lst.append(h-y)
diff_lst.append(y-0)

# 그 차가 제일 작은거 출력
print(min(diff_lst))