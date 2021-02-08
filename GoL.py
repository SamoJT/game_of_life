import tkinter as tk
from random import randrange

def create_grid(w, h, buf):
    vert = 0
    hori = 0
    for i in range(buf, w, buf):
        canvas.create_line(i, buf, i, h-buf)  # (x0, y0, x1, y1) Vert
        vert += 1
    for i in range(buf, h, buf):
        canvas.create_line(buf, i, w-buf, i)  # Horiz
        hori += 1
    print(f'Cols = {vert-1}\nRows = {hori-1}')
    return

def initialise(seed, w, h, buf):
    coords = set()
    while len(coords) < seed:
        coords.add((randrange(buf,w-buf,buf), (randrange(buf,h-buf,buf))))
    # print(coords)
    return coords

def fill_squares(coords, buf):
    # Takes a set or list containing sets of coordinates.
    try:
        canvas.delete('alive')
    except:
        pass
    for i in coords:
        x0 = i[0]
        y0 = i[1]        
        x1 = x0+buf
        y1 = y0+buf
        canvas.create_rectangle(x0, y0, x1, y1, fill='black', tags=('alive'))
    return

def get_state(w, h, buf, coords):
    rows = [[]for i in range(buf, w-buf, buf)]
    x0 = buf
    y0 = buf
    row = buf
    index = 0
    while row < h-buf:
        # print(f'Debug -- index: {index}')
        for i in range(buf, w-buf, buf):
            x0 = i
            xy = (x0,y0)
            # print(f'Debug -- (x0,y0): {xy}')
            if xy in coords:
                rows[index].append(1)
            else:
                rows[index].append(0)
        y0 += buf
        row = y0
        index += 1
    return rows

def update_state(w, h, buf, old_cell_states):
    index = 0
    row_num = 0
    new_cell_states = []
    alive_n = 0
    
    for row in old_cell_states:
        y0 = ((row_num+1)* 10)*(buf/10)
        for val in row:
            try:
                alive_n += old_cell_states[row_num][index-1]
            except:
                continue
            try:
                alive_n += old_cell_states[row_num][index+1]
            except:
                continue
            try:      
                alive_n += old_cell_states[row_num-1][index]
            except:
                continue
            try:
                alive_n += old_cell_states[row_num-1][index-1]
            except:
                continue
            try:
                alive_n += old_cell_states[row_num-1][index+1]
            except:
                continue
            try:
                alive_n += old_cell_states[row_num+1][index]
            except:
                continue
            try:
                alive_n += old_cell_states[row_num+1][index-1]
            except:
                continue
            try:
                alive_n += old_cell_states[row_num+1][index+1]
            except:
                continue
            
            x0 = ((index+1)*10)*(buf/10)
            if val and 1 < alive_n < 4:
                new_cell_states.append((x0,y0))
            elif not val and alive_n == 3:
                new_cell_states.append((x0,y0))
            
            alive_n = 0            
            # print((x0,y0), val)
            index += 1
        index = 0
        row_num += 1
    return new_cell_states
  
def main_loop(w, h, buf, coords):
    fill_squares(coords, buf)
    cell_states = get_state(w, h, buf, coords)
    coords = update_state(w, h, buf, cell_states)
    root.after(100, main_loop, w, h, buf, coords)


w = 500 # 500 min Width and height
h = 500
buf = 20  # Edge buffer needs to be divisible by w and h
seed = 350 # Starting amount of cells

    
    
if w < 500 or h < 500:
    raise ValueError('Minimum 500x500 size')
if w % buf != 0 or h % buf != 0:
    raise ValueError('Buffer value must be divisible by width and height')

root = tk.Tk()
canvas = tk.Canvas(root, width=w, height=h, background='white')

create_grid(w, h, buf)
coords = initialise(seed, w, h, buf)
main_loop(w, h, buf, coords)

canvas.pack()
root.mainloop()