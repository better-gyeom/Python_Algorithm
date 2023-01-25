prices = []
total_price = []

for n in range(5):
    price = int(input()) # 버거의 값 3개와 음료 값 2개 입력 받기
    prices.append(price) 

for burger in prices[:3]:
    for drink in prices[3:]:
        total_price.append((burger + drink) - 50) # 이중 for문을 통해 가능한 세트 가격을 만들고, 50원을 뺀 리스트 만들기
        
print(min(total_price)) # 세트 가격 최솟값