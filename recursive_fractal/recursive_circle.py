import tkinter as tk


SHAPE = 800
INDENT = 20
OUTLINE_COLOR = 'white'
MAX_RECURSION = 4


def draw_fractal(canvas: tk.Canvas, center_x: int, center_y: int, radius: (int, float), max_depth, depth=1):
    x1 = center_x - radius + INDENT
    y1 = center_y - radius + INDENT
    x2 = center_x + radius - INDENT
    y2 = center_y + radius - INDENT
    canvas.create_oval(x1, y1, x2, y2, outline=OUTLINE_COLOR)
    if depth <= max_depth:
        new_center_x_left = center_x - radius // 2 + INDENT // 2
        new_center_x_right = center_x + radius // 2 - INDENT // 2
        new_radius = radius // 2.2
        draw_fractal(canvas, new_center_x_left, center_y, new_radius, max_depth, depth=depth+1)
        draw_fractal(canvas, new_center_x_right, center_y, new_radius, max_depth, depth=depth+1)


def main():
    root = tk.Tk()
    root.geometry('800x800+20+20')
    canvas = tk.Canvas(root, width=SHAPE, height=SHAPE, bg='#1E1E1E')
    canvas.pack()
    draw_fractal(canvas, SHAPE // 2, SHAPE // 2, SHAPE // 2, MAX_RECURSION)
    tk.mainloop()


if __name__ == '__main__':
    main()
