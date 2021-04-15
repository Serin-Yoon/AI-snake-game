from drawingpanel import *

def cars(panel, x, y):
    panel.canvas.create_rectangle(x, y, x + 100, y + 50, fill="black")
    panel.canvas.create_oval(x + 10, y + 40, x + 30, y + 60, fill="red")
    panel.canvas.create_oval(x + 70, y + 40, x + 90, y + 60, fill="red")
    panel.canvas.create_rectangle(x + 70, y + 10, x + 100, y + 30, fill="cyan")

panel = DrawingPanel(500, 300)
panel.set_background("gray")

cars(panel, 10, 10)
cars(panel, 10, 100)
cars(panel, 10, 190)
cars(panel, 150, 10)
cars(panel, 150, 100)
cars(panel, 150, 190)
cars(panel, 290, 10)