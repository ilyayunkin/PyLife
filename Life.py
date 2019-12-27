import time
from random import *
from LifeGui import LifeGui


class Life:
    def __init__(self, lines_count):
        self.lines_count = lines_count
        self.points_list = list()
        self.gui = LifeGui(lines_count, self.points_list)
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

    def play(self):
        while True:
            self.update_cells()
            self.gui.redraw()
            time.sleep(1)
