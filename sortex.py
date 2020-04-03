
nums = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for number in range(len(nums)):
    if nums[number] < 60:
        continue
    print("%d번 학생 합격입니다" % (number+1))

