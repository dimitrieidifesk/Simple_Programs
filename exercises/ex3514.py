first_place_x = int(input("first_place_x: "))
first_place_y = int(input("first_place_y: "))
second_place_x = int(input("second_place_x: "))
second_place_y = int(input("second_place_y: "))

if max(first_place_x-second_place_x, -(first_place_x-second_place_x)) == max(first_place_y-second_place_y, -(first_place_y-second_place_y)):
    print ('YES')
else:
    print ('NO')


