import time
from random import *
from tkinter import *


class Life:
    def __init__(self, lines_count):
        self.lines_count = lines_count
        self.cell_width = 30
        self.size = lines_count * self.cell_width
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.size, height=self.size)
        self.canvas.pack()
        self.points_list = list()
        for i in range(self.lines_count * self.lines_count):
            a = randint(0, 10)
            if a < 3:
                self.points_list.append(True)
            else:
                self.points_list.append(False)

    def coord_to_pos(self, x, y):
        pos = y * self.lines_count + x
        return pos

    def if_true(self, list1, x, y):
        pos = self.coord_to_pos(x, y)
        if (pos >= 0) and (pos < (self.lines_count * self.lines_count)):
            return list1[pos]
        else:
            return False

    def count_nei(self, list1, pos):
        nei = 0
        x = int(pos % self.lines_count)
        y = int(pos / self.lines_count)
        if self.if_true(list1, x + 1, y):
            nei = nei + 1
        if self.if_true(list1, x + 1, y + 1):
            nei = nei + 1
        if self.if_true(list1, x + 1, y - 1):
            nei = nei + 1
        if self.if_true(list1, x, y + 1):
            nei = nei + 1
        if self.if_true(list1, x, y - 1):
            nei = nei + 1
        if self.if_true(list1, x - 1, y):
            nei = nei + 1
        if self.if_true(list1, x - 1, y + 1):
            nei = nei + 1
        if self.if_true(list1, x - 1, y - 1):
            nei = nei + 1
        return nei

    def update_cells(self):
        list_for_del = list()
        list_for_add = list()
        for i in range(self.lines_count * self.lines_count):
            nei_count = self.count_nei(self.points_list, i)
            if self.points_list[i]:
                if not (nei_count == 3 or nei_count == 2):
                    list_for_del.append(i)
            else:
                if nei_count == 3:
                    list_for_add.append(i)
        for i in list_for_add:
            self.points_list[i] = True
        for i in list_for_del:
            self.points_list[i] = False

    def redraw(self):
        self.canvas.delete("all")
        for i in range(self.lines_count * self.lines_count):
            if self.points_list[i]:
                x = int(i % self.lines_count)
                y = int(i / self.lines_count)
                colors = 'green'
                x0 = x * self.cell_width
                y0 = y * self.cell_width
                self.canvas.create_rectangle(x0, y0, x0 + self.cell_width, y0 + self.cell_width, fill=colors)
        self.root.update()

    def play(self):
        while True:
            self.update_cells()
            self.redraw()
            time.sleep(1)
