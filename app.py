import time
from random import *
from tkinter import *

lines_count = 20
cell_width = 30
size = lines_count * cell_width
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
diapason = 0


def coord_to_pos(x, y):
    pos = y * lines_count + x
    return pos

def if_true(list1, x, y):
    pos = coord_to_pos(x, y)
    if (pos >= 0) and (pos < (lines_count * lines_count)):
        return list1[pos]
    else:
        return False

def count_nei(list1, pos):
    nei = 0
    x = int(pos % lines_count)
    y = int(pos / lines_count)
    if if_true(list1, x + 1, y):
        nei = nei + 1
    if if_true(list1, x + 1, y + 1):
        nei = nei + 1
    if if_true(list1, x + 1, y - 1):
        nei = nei + 1
    if if_true(list1, x, y + 1):
        nei = nei + 1
    if if_true(list1, x, y - 1):
        nei = nei + 1
    if if_true(list1, x - 1, y):
        nei = nei + 1
    if if_true(list1, x - 1, y + 1):
        nei = nei + 1
    if if_true(list1, x - 1, y - 1):
        nei = nei + 1
    return nei

points_list = list()
for i in range(lines_count * lines_count):
    a = randint(0, 10)
    if a < 3:
        points_list.append(True)
    else:
        points_list.append(False)

while True:
    list_for_del = list()
    list_for_add = list()
    for i in range(lines_count * lines_count):
        nei_count = count_nei(points_list, i)
        if points_list[i]:
            if not( nei_count == 3 or nei_count == 2):
                list_for_del.append(i)
        else:
            if nei_count == 3:
                list_for_add.append(i)
    for i in list_for_add:
        points_list[i] = True
    for i in list_for_del:
        points_list[i] = False

    canvas.delete("all")
    for i in range(lines_count * lines_count):
        if points_list[i]:
            x = i % lines_count
            y = i / lines_count
            colors = 'green'
            x0 = x * cell_width
            y0 = y * cell_width
            canvas.create_rectangle(x0, y0, x0 + cell_width, y0 + cell_width, fill=colors)
    root.update()
    time.sleep(1)
