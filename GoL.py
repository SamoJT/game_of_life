import tkinter as tk
from random import randrange

def create_grid(w, h, buf):
    row_and_cols = 0
    for i in range(buf, w, 20):
        canvas.create_line(i, buf, i, h-buf)  # (x0, y0, x1, y1)
        canvas.create_line(buf, i, w-buf, i)
        row_and_cols += 1
    print(f'Debug -- Amount of Rows and cols: {row_and_cols}')
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

def get_state(w, h, buf, coords):
    rows = [[]for i in range(buf, w-buf, 20)]
    x0 = buf
    y0 = buf
    row = buf
    while row < 800:
        index = int((row/2)/10-1)
        # print(f'Debug -- index: {index}')
        for i in range(buf, w-buf, 20):
            x0 = i
            xy = (x0,y0)
            # print(f'Debug -- (x0,y0): {xy}')
            if xy in coords:
                rows[index].append('Alive')
            else:
                rows[index].append('Dead')
        y0 += 20
        row = y0
    print(rows)

root = tk.Tk()
w = 820
h = 820
buf = 20  # Edge buffer
canvas = tk.Canvas(root, width=w, height=h, background='white')

create_grid(w, h, buf)
coords = initialise()
# print(f'Debug -- Alive: {len(coords)}')
fill_squares(coords)
get_state(w, h, buf, coords)




canvas.pack()
root.mainloop()