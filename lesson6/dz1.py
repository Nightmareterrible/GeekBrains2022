from tkinter import *


class TrafficLight(Tk):

    def running(self):
        self.canvas.itemconfigure(self.r, fill='red' if self.color == 0 else "black")
        self.canvas.itemconfigure(self.y, fill='yellow' if self.color == 1 else "black")
        self.canvas.itemconfigure(self.g, fill='green' if self.color == 2 else "black")
        print(self.color)
        self.after(7000 if self.color == 0 else 2000 if self.color == 1 else 5000, self.running)
        self.color = self.color + 1 if self.color < 2 else 0

    def __init__(self):
        self.color = 0
        super().__init__()
        self.title('Светофор')
        self.canvas = c = Canvas(self, width=70, height=190, bg="black")
        self.r = c.create_oval(10, 10, 60, 60, fill='red')
        self.y = c.create_oval(10, 70, 60, 120, fill='yellow')
        self.g = c.create_oval(10, 130, 60, 180, fill='green')
        c.pack()
        self.update()


okno = TrafficLight()
okno.running()
okno.mainloop()
