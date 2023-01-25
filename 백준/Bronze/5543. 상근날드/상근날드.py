
burger_price = []
drink_price = []
set_price = []

#for문을 따로따로 선언하면 관리하기 수월하다.
for _ in range(3):
    price = int(input()) 
    burger_price.append(price)

for _ in range(2):
    price = int(input())
    drink_price.append(price)

for burger in burger_price:
    for drink in drink_price:
        set_price.append((burger + drink) - 50) # 이중 for문을 통해 가능한 세트 가격을 만들고, 50원을 뺀 리스트 만들기
        
print(min(set_price)) # 세트 가격 최솟값