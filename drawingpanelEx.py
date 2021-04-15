from drawingpanel import *

# panel
panel = DrawingPanel(400, 300)

# background
panel.set_background("yellow")

# line (x1, y1, x2, y2)
panel.canvas.create_line(10, 30, 200, 30)

# oval (x1, y1, x2, y2)
panel.canvas.create_oval(10, 60, 50, 120)

# rectangle (x1, y1, x2, y2)
panel.canvas.create_rectangle(100, 50, 200, 200, outline="red", fill="green")

# string (x, y)
panel.canvas.create_text(250, 90, text="hello")

# polygon (x1, y1, x2, y2, x3, y3)
panel.canvas.create_polygon(300, 100, 350, 50, 350, 150)

# java와 달리 fillRect, fillOval, setColor 없음
# 대신 outline, fill 사용