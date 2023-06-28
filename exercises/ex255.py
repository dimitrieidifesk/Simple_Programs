elephant_x = int(input("elephant_x: "))
elephant_y = int(input("elephant_y: "))
some_figure_x = int(input("some_figure_x: "))
some_figure_y = int(input("some_figure_y: "))


if max(elephant_x-some_figure_x, -(elephant_x-some_figure_x)) == max(elephant_y-some_figure_y, -(elephant_y-some_figure_y)):
    print ('YES')
else:
    print ('NO')

