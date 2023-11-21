import tkinter as tk
from tkinter import ttk
import math


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Gráfico Interativo Básico")

        self.selected_shape = "rectangle"
        self.selected_color = "yellow"
        self.fill_var = tk.IntVar()
        self.size_var = tk.StringVar()
        self.last_shape_id = None
        self.rotate_interval = 10  # Intervalo de rotação em graus
        self.move_distance = 10  # Distância de movimento

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.create_shape_buttons()
        self.create_color_combobox()
        self.create_fill_checkbox()
        self.create_size_entry()
        self.create_rotate_buttons()
        self.create_clear_button()

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Button-3>", self.delete_shape)
        self.root.bind("<Up>", lambda event: self.move_shape(
            0, -self.move_distance))
        self.root.bind("<Down>", lambda event: self.move_shape(
            0, self.move_distance))
        self.root.bind(
            "<Left>", lambda event: self.move_shape(-self.move_distance, 0))
        self.root.bind("<Right>", lambda event: self.move_shape(
            self.move_distance, 0))

        self.root.after(10, self.set_initial_combobox_selection)
        self.fill_var.set(1)  # Pré-seleção checkbox
        self.size_var.set("155")  # Pré-configuração tamanho

    def create_shape_buttons(self):
        shapes_frame = ttk.Frame(self.root)
        shapes_frame.pack(side=tk.LEFT, padx=10, pady=10)

        ttk.Button(shapes_frame, text="Retângulo", command=lambda: self.set_shape(
            "rectangle"), width=15).pack(pady=5)
        ttk.Button(shapes_frame, text="Círculo", command=lambda: self.set_shape(
            "circle"), width=15).pack(pady=5)
        ttk.Button(shapes_frame, text="Reta", command=lambda: self.set_shape(
            "line"), width=15).pack(pady=5)
        ttk.Button(shapes_frame, text="Triângulo", command=lambda: self.set_shape(
            "triangle"), width=15).pack(pady=5)
        ttk.Button(shapes_frame, text="Quadrado", command=lambda: self.set_shape(
            "square"), width=15).pack(pady=5)

    def create_color_combobox(self):
        color_frame = ttk.Frame(self.root)
        color_frame.pack(side=tk.LEFT, padx=10, pady=10)

        ttk.Label(color_frame, text="Escolha uma cor:",
                  font=("Arial", 12)).pack()

        colors = ["yellow", "blue", "orange",
                  "brown", "pink", "purple", "green", "red"]
        colors.sort()

        self.color_var = tk.StringVar()
        color_combobox = ttk.Combobox(
            color_frame, textvariable=self.color_var, values=colors, state="readonly", font=("Arial", 12))
        color_combobox.pack(pady=5)

        color_combobox.bind("<<ComboboxSelected>>",
                            lambda event: self.set_color(self.color_var.get()))

    def create_fill_checkbox(self):
        fill_frame = ttk.Frame(self.root)
        fill_frame.pack(side=tk.LEFT, padx=10, pady=10)

        fill_checkbox = ttk.Checkbutton(
            fill_frame, text="Preencher", variable=self.fill_var, onvalue=1, offvalue=0)
        fill_checkbox.pack()

    def create_size_entry(self):
        size_frame = ttk.Frame(self.root)
        size_frame.pack(side=tk.LEFT, padx=10, pady=10)

        ttk.Label(size_frame, text="Escala:",
                  font=("Arial", 12)).pack()
        size_entry = ttk.Entry(
            size_frame, textvariable=self.size_var, font=("Arial", 12))
        size_entry.pack(pady=5)

    def create_rotate_buttons(self):
        rotate_frame = ttk.Frame(self.root)
        rotate_frame.pack(side=tk.LEFT, padx=10, pady=10)

        rotate_right_button = ttk.Button(
            rotate_frame, text="Girar para a Direita", command=self.rotate_right, width=20)
        rotate_right_button.pack(pady=5)
        rotate_right_button.bind(
            "<ButtonPress-1>", self.start_rotation_right)
        rotate_right_button.bind(
            "<ButtonRelease-1>", self.stop_rotation)

        rotate_left_button = ttk.Button(
            rotate_frame, text="Girar para a Esquerda", command=self.rotate_left, width=20)
        rotate_left_button.pack(pady=5)
        rotate_left_button.bind(
            "<ButtonPress-1>", self.start_rotation_left)
        rotate_left_button.bind(
            "<ButtonRelease-1>", self.stop_rotation)

        self.rotating = False

    def create_clear_button(self):
        clear_frame = ttk.Frame(self.root)
        clear_frame.pack(side=tk.LEFT, padx=10, pady=10)

        clear_button = ttk.Button(
            clear_frame, text="Limpar Tela", command=self.clear_canvas, width=20)
        clear_button.pack(pady=5)

    def set_shape(self, shape):
        self.selected_shape = shape

    def set_color(self, color_name):
        self.selected_color = color_name

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        fill_option = tk.YES if self.fill_var.get() == 1 else tk.NO
        size = int(self.size_var.get()) if self.size_var.get() else 0

        if self.selected_shape == "rectangle":
            shape_id = self.draw_shape("rectangle", x, y, size)
        elif self.selected_shape == "circle":
            shape_id = self.draw_shape("circle", x, y, size)
        elif self.selected_shape == "line":
            shape_id = self.draw_shape("line", x, y, size)
        elif self.selected_shape == "triangle":
            shape_id = self.draw_shape("triangle", x, y, size)
        elif self.selected_shape == "square":
            shape_id = self.draw_shape("square", x, y, size)

        self.last_shape_id = shape_id

    def delete_shape(self, event):
        x, y = event.x, y = event.y
        item = self.canvas.find_closest(x, y)
        self.canvas.delete(item)

    def draw_shape(self, shape, x, y, size):
        fill_option = tk.YES if self.fill_var.get() == 1 else tk.NO

        if shape == "rectangle":
            return self.canvas.create_rectangle(x - size, y - size//2, x + size, y + size//2, fill=self.selected_color if fill_option else "", outline=self.selected_color)
        elif shape == "circle":
            return self.canvas.create_oval(x - size//2, y - size//2, x + size//2, y + size//2, fill=self.selected_color if fill_option else "", outline=self.selected_color)
        elif shape == "line":
            length = size if size else 50
            x2 = x + length
            return self.canvas.create_line(x, y, x2, y, width=3, fill=self.selected_color)
        elif shape == "triangle":
            return self.canvas.create_polygon(x, y - size//2, x - size//2, y + size//2, x + size//2, y + size//2, fill=self.selected_color if fill_option else "", outline=self.selected_color)
        elif shape == "square":
            return self.canvas.create_rectangle(x - size//2, y - size//2, x + size//2, y + size//2, fill=self.selected_color if fill_option else "", outline=self.selected_color)

    def clear_canvas(self):
        self.canvas.delete("all")

    def rotate_right(self):
        self.rotate_shape("right")
        if self.rotating:
            self.root.after(50, self.rotate_right)

    def rotate_left(self):
        self.rotate_shape("left")
        if self.rotating:
            self.root.after(50, self.rotate_left)

    def start_rotation_right(self, event=None):
        self.rotating = True
        self.rotate_right()

    def start_rotation_left(self, event=None):
        self.rotating = True
        self.rotate_left()

    def stop_rotation(self, event=None):
        self.rotating = False

    def move_shape(self, dx, dy):
        if self.last_shape_id is not None:
            self.canvas.move(self.last_shape_id, dx, dy)

    def rotate_shape(self, direction):
        if self.last_shape_id is not None:
            angle = math.radians(
                self.rotate_interval) if direction == "right" else -math.radians(self.rotate_interval)

            coords = self.canvas.coords(self.last_shape_id)

            cx, cy = self.calculate_shape_center(coords)

            rotated_coords = self.rotate_shape_coords(cx, cy, angle, *coords)

            self.canvas.coords(self.last_shape_id, *rotated_coords)

    def calculate_shape_center(self, coords):
        if self.selected_shape in ["rectangle", "square"]:
            cx = (coords[0] + coords[2]) / 2
            cy = (coords[1] + coords[3]) / 2
        elif self.selected_shape in ["circle"]:
            cx = (coords[0] + coords[2]) / 2
            cy = (coords[1] + coords[3]) / 2
        elif self.selected_shape in ["line"]:
            cx = (coords[0] + coords[2]) / 2
            cy = (coords[1] + coords[3]) / 2
        elif self.selected_shape in ["triangle"]:
            cx = (coords[0] + coords[2] + coords[4]) / 3
            cy = (coords[1] + coords[3] + coords[5]) / 3
        elif self.selected_shape in ["circle"]:
            cx = (coords[0] + coords[2]) / 2
            cy = (coords[1] + coords[3]) / 2
        elif self.selected_shape in ["square"]:
            cx = (coords[0] + coords[2]) / 2
            cy = (coords[1] + coords[3]) / 2
        else:
            cx = 0
            cy = 0

        return cx, cy

    def rotate_shape_coords(self, cx, cy, angle, *coords):
        rotated_coords = []
        for i in range(0, len(coords), 2):
            x = coords[i]
            y = coords[i + 1]

            x_new = cx + (x - cx) * math.cos(angle) - \
                (y - cy) * math.sin(angle)
            y_new = cy + (x - cx) * math.sin(angle) + \
                (y - cy) * math.cos(angle)

            rotated_coords.extend([x_new, y_new])

        return rotated_coords

    def set_initial_combobox_selection(self):
        self.color_var.set("yellow")


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
