
# 10년 복리
# 1999년 10% 금리, 10억

money = 1000
rate = 0.0075

# count = 1

# while count <= 10:
#
#     money = money + (money * rate)
#
#     print(count, money)
#
#     count += 1

for x in range(1, 11):

    money = money + (money * rate)

    print(x, money)

list=[123, "str", a=0]