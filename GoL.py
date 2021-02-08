import tkinter as tk
from random import randrange

def create_grid(w, h, buf):
    for i in range(buf, w, 20):
        canvas.create_line(i, buf, i, h-buf)  # (x0, y0, x1, y1)
        canvas.create_line(buf, i, w-buf, i)
    return

def initialise():
    coords = set()
    while len(coords) < 300:
        coords.add((randrange(20,800,20), (randrange(20,800,20))))
    # print(coords)
    return coords

def fill_squares(coords):
    for i in coords:
        x0 = i[0]
        y0 = i[1]        
        x1 = x0+20
        y1 = y0+20
        canvas.create_rectangle(x0, y0, x1, y1, fill='red')
    return

def check_squares(w, h, buf, coords):
    pass      

root = tk.Tk()
w = 820
h = 820
buf = 20  # Edge buffer
canvas = tk.Canvas(root, width=w, height=h, background='white')

create_grid(w, h, buf)
coords = initialise()
print(f'Debug -- Alive: {len(coords)}')
fill_squares(coords)
check_squares(w, h, buf, coords)




canvas.pack()
root.mainloop()