import math

movie_samle = [
   ('A',5,15),
   ('A',10,20),
   ('A',15,20),
   ('A',15,15),
   ('M',20,15),
   ('M',20,10),
   ('M',20,5),
   ('M',15,5)
]

def calcDistance(point1, point2):
   result = math.sqrt(math.pow(point1[1] - point2[0],2 ) +
                       math.pow(point1[2] - point2[1],2))

   return result

count_kiss = int(input("키스씬"))
count_action = int(input("액션씬"))

target = (count_kiss, count_action)

movie_samle.sort(key= lambda m:calcDistance(m, target))

print(movie_samle)

result_movies = movie_samle[0:3]

print(result_movies)

count_m = 0
count_a = 0

for m in result_movies:

   if m[0] == 'A':
       count_a += 1

   elif m[0] == 'M':
       count_m += 1

if count_m > count_a:
   print("멜로영화입니다.")
else:
   print("액션영화입니다.")