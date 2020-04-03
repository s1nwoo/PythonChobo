import random

balls = [ x for x in range(1,46)]

random.shuffle(balls)

result = balls[0:6]

print(sorted(result))
