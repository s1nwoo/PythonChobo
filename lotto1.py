# 1-45까지 6가지 숫자 무작위 , 중복 X
from random import  randrange
nums = []

def checkDuplicate(num_list, target):

    result = False

    for x in num_list:
        if x == target:
            result = True
            break
    return result

# 루프를 nums 가 6개가 되는 동안
while len(nums) < 6:
    #1부터 45 사이의 숫자를 뽑는다
    num = randrange(1,46)
    # 뽑힌 숫자가 있는지 확인

     if num not in nums:
         nums.append(num)

print(nums)
# 1부터 45 사이의 숫자를 뽑는다

# 뽑은 값이 있다면 다시 뽑는다

#

