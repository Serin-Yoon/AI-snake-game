from drawingpanel import *

def cars(panel, x, y):
    for i in range(10):
        panel.canvas.create_rectangle(0, 0, 700, 700, fill="white")

        panel.canvas.create_rectangle(x[0] * i, y[0], x[0] * i + 100, y[0] + 50, fill="black")
        panel.canvas.create_oval(x[0] * i + 10, y[0] + 40, x[0] * i + 30, y[0] + 60, fill="red")
        panel.canvas.create_oval(x[0] * i + 70, y[0] + 40, x[0] * i + 90, y[0] + 60, fill="red")
        panel.canvas.create_rectangle(x[0] * i + 70, y[0] + 10, x[0] * i + 100, y[0] + 30, fill="cyan")

        panel.canvas.create_rectangle(x[1] * i, y[1], x[1] * i + 100, y[1] + 50, fill="black")
        panel.canvas.create_oval(x[1] * i + 10, y[1] + 40, x[1] * i + 30, y[1] + 60, fill="red")
        panel.canvas.create_oval(x[1] * i + 70, y[1] + 40, x[1] * i + 90, y[1] + 60, fill="red")
        panel.canvas.create_rectangle(x[1] * i + 70, y[1] + 10, x[1] * i + 100, y[1] + 30, fill="cyan")

        panel.canvas.create_rectangle(x[2] * i, y[2], x[2] * i + 100, y[2] + 50, fill="black")
        panel.canvas.create_oval(x[2] * i + 10, y[2] + 40, x[2] * i + 30, y[2] + 60, fill="red")
        panel.canvas.create_oval(x[2] * i + 70, y[2] + 40, x[2] * i + 90, y[2] + 60, fill="red")
        panel.canvas.create_rectangle(x[2] * i + 70, y[2] + 10, x[2] * i + 100, y[2] + 30, fill="cyan")

        panel.canvas.create_rectangle(x[3] * i, y[3], x[3] * i + 100, y[3] + 50, fill="black")
        panel.canvas.create_oval(x[3] * i + 10, y[3] + 40, x[3] * i + 30, y[3] + 60, fill="red")
        panel.canvas.create_oval(x[3] * i + 70, y[3] + 40, x[3] * i + 90, y[3] + 60, fill="red")
        panel.canvas.create_rectangle(x[3] * i + 70, y[3] + 10, x[3] * i + 100, y[3] + 30, fill="cyan")
        panel.sleep(200)

panel = DrawingPanel(600, 350)

cars(panel, [100, 100, 100, 100], [10, 100, 190, 280])