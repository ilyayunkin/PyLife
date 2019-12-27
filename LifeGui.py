from tkinter import *


class LifeGui:
    def __init__(self, lines_count, points_list):
        self.points_list = points_list
        self.lines_count = lines_count
        self.cell_width = 30
        self.size = lines_count * self.cell_width
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.size, height=self.size)
        self.canvas.pack()

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
