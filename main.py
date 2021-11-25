from tkinter import Tk, Canvas, Frame, BOTH
from random import randint as rand
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Рисуем линии")
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
        def circle_coord(x,y):
            return [x-1, y, x, y+1]

        def center(a, b):
            return [(a[0]+b[0])/2,(a[1]+b[1])/2]

        def circle(x, y):
            canvas.create_oval(
            circle_coord(x, y), outline="red", 
            fill="green", width=2
            )

        a1 = [200, 200]
        canvas.create_text(
            200, 200-10, font="Arial",
            text="A1"
        )
        a2 = [500, 700]
        canvas.create_text(
            500, 700+10, font="Arial",
            text="A2"
        )
        a3 = [800, 200]
        canvas.create_text(
            800, 200-10, font="Arial",
            text="A3"
        )
        x = [rand(0, 1000), rand(0, 800)]
        canvas.create_text(
            x[0], x[1]+10, font="Arial",
            text="X0"
        )
        canvas.create_line(a1, a2, a2, a3, a3, a1)
        circle(x[0], x[1])

        for i in range(0, 5000):
            dot = rand(1, 3)
            if dot == 1:
                x = [center(a1, x)[0], center(a1, x)[1]]
            if dot == 2:
                x = [center(a2, x)[0], center(a2, x)[1]]
            if dot == 3:
                x = [center(a3, x)[0], center(a3, x)[1]]
            
            circle(x[0], x[1])

        canvas.pack(fill=BOTH, expand=1)
 
def main():
    root = Tk()
    ex = Example()
    root.geometry("1000x800")
    root.mainloop()
 
if __name__ == '__main__':
    main()
