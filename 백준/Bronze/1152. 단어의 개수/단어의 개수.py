
sentence = input()
print(len(sentence.split()))

# 아래는 삽질한 흔적.... 공백에만 너무 집중해서 split를 전혀 생각하지 못했다.
# 맨날 입력받을 때 쓰는게 split인데...............
# 앞으론 뜻을 잘 기억하고 써야겠다.. 그냥 무작정 쓰지 않고...

# sentence_lst = []
# count = 0

# for sen in sentence:
#     sentence_lst.append(sen)


# for sen_l in sentence_lst:
#     if str(sen_l) == ' ':
#         count += 1
# print(count)

# if str(sentence_lst[0]) == ' ':
#     count -= 1
#     print(count)
# elif str(sentence_lst[-1]) == ' ':
#     count -= 2
#     print(count)

# # if str(sentence_lst[0]) == ' ' or str(sentence_lst[-1]) == ' ':
# #     count -= 1

# print(count+1)

