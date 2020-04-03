from random import randrange

result_list = 0

for x in range(10):
    user = int(input("가위 0, 바위 1, 보 2 \n"))

    com = randrange(0, 3)

    if user > com:
        com = com + 3

    result = com - user

    result = ''

    print(user, com, result)

    if result == 2:
        result = "U"
    elif result == 1:
        result = "C"
    else:
        result = "D"

    result_list.append(result)



