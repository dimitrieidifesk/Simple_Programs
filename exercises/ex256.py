queen_x = int(input("queen_x: "))
queen_y = int(input("queen_y: "))
some_figure_x = int(input("some_figure_x: "))
some_figure_y = int(input("some_figure_y: "))


if max(queen_x-some_figure_x, -(queen_x-some_figure_x)) == max(queen_y-some_figure_y, -(queen_y-some_figure_y)):
    print ('YES')
elif queen_x == some_figure_x:
    print ('YES')
elif queen_y == some_figure_y:
    print ('YES')
else:
    print ('NO')
