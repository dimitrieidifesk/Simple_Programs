lesson = int(input())
lesson = lesson*45 + (lesson//2)*5 + ((lesson+1)//2-1)*15
print(lesson//60 + 9, lesson%60)



