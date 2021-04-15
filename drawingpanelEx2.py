from drawingpanel import *

panel = DrawingPanel(350, 300)
for i in range(20):
    # clear any previous image
    panel.canvas.create_rectangle(0, 0, 400, 400, outline="white", fill="white")

    panel.canvas.create_polygon(20 * i, 50, 20 * i, 100, 20 * i + 50, 75)
    panel.sleep(100) # pause the panel by calling sleep

