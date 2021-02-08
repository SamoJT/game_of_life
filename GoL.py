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

def initialise(seed):
    coords = set()
    while len(coords) < seed:
        coords.add((randrange(20,800,20), (randrange(20,800,20))))
    # print(coords)
    return coords

def fill_squares(coords):
    # Takes a set or list containing sets of coordinates.
    try:
        canvas.delete('alive')
    except:
        pass
    for i in coords:
        x0 = i[0]
        y0 = i[1]        
        x1 = x0+20
        y1 = y0+20
        canvas.create_rectangle(x0, y0, x1, y1, fill='red', tags=('alive'))
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
                rows[index].append(1)
            else:
                rows[index].append(0)
        y0 += 20
        row = y0
    return rows

def update_state(w, h, buf, old_cell_states):
    index = 0
    row_num = 0
    new_cell_states = []
    alive_n = 0
    
    for row in old_cell_states:
        y0 = ((row_num+1)* 10)*2
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
            x0 = ((index+1)*10)*2
            if 1 < alive_n > 4 and val == 1:
                new_cell_states.append((x0,y0))
            elif alive_n == 3 and val == 0:
                new_cell_states.append((x0,y0))
            alive_n = 0            
            # print((x0,y0), val)
            index += 1
        index = 0
        row_num += 1
    return new_cell_states
  
def main_loop(w, h, buf, coords):
    fill_squares(coords)
    cell_states = get_state(w, h, buf, coords)
    coords = update_state(w, h, buf, cell_states)
    root.after(500, main_loop, w, h, buf, coords)


w = 820
h = 820
buf = 20  # Edge buffer
seed = 700 # Starting amount of cells

root = tk.Tk()
canvas = tk.Canvas(root, width=w, height=h, background='white')

create_grid(w, h, buf)
coords = initialise(seed)
main_loop(w, h, buf, coords)

canvas.pack()
root.mainloop()
