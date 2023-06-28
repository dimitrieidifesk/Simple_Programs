hourse_x = int(input("hourse_x: "))
hourse_y = int(input("hourse_y: "))
some_figure_x = int(input("some_figure_x: "))
some_figure_y = int(input("some_figure_y: "))

if max(hourse_y-some_figure_y, -(hourse_y-some_figure_y)) == 2:
    if max(hourse_x-some_figure_x, -(hourse_x-some_figure_x)) == 1:
        print ('YES')
    else:
        print ('NO')

elif max(hourse_y-some_figure_y, -(hourse_y-some_figure_y)) == 1:
    if max(hourse_x-some_figure_x, -(hourse_x-some_figure_x)) == 2:
        print ('YES')
    else:
        print ('NO')

else:
    print ('NO')