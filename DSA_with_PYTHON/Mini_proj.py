import tkinter as tk
import random
from tkinter import messagebox, font

class MazeApp:
    def __init__(self, root, rows=20, cols=20, cell_size=25):  # Fixed: __init__
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        # Cute game title
        title_font = font.Font(family="Comic Sans MS", size=24, weight="bold")
        self.title_label = tk.Label(root, text="Maze Adventure!!", font=title_font, fg="purple")
        self.title_label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
        self.canvas.pack()

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Generate Maze", command=self.generate_new_maze, bg="lightblue").pack(side=tk.LEFT, padx=5)

        self.grid = None
        self.start = (0, 0)
        self.end = (rows - 1, cols - 1)
        self.player = None
        self.player_rect = None

        self.generate_new_maze()

        # Keyboard controls
        self.root.bind("<Up>", lambda e: self.move_player(-1, 0))
        self.root.bind("<Down>", lambda e: self.move_player(1, 0))
        self.root.bind("<Left>", lambda e: self.move_player(0, -1))
        self.root.bind("<Right>", lambda e: self.move_player(0, 1))

    def generate_new_maze(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.generate_maze(0, 0)
        self.player = self.start
        self.draw_maze()
        self.draw_player()

    def generate_maze(self, r, c):
        self.visited[r][c] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and not self.visited[nr][nc]:
                self.grid[r][c] |= self.dir_to_bit(dr, dc)
                self.grid[nr][nc] |= self.dir_to_bit(-dr, -dc)
                self.generate_maze(nr, nc)

    def dir_to_bit(self, dr, dc):
        if dr == 0 and dc == 1: return 1
        if dr == 1 and dc == 0: return 2
        if dr == 0 and dc == -1: return 4
        if dr == -1 and dc == 0: return 8

    def draw_maze(self):
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                cell = self.grid[r][c]
                if not (cell & 1):  # right wall
                    self.canvas.create_line(x2, y1, x2, y2, fill="black", width=2)
                if not (cell & 2):  # bottom wall
                    self.canvas.create_line(x1, y2, x2, y2, fill="black", width=2)
                if not (cell & 4):  # left wall
                    self.canvas.create_line(x1, y1, x1, y2, fill="black", width=2)
                if not (cell & 8):  # top wall
                    self.canvas.create_line(x1, y1, x2, y1, fill="black", width=2)
        self.highlight_cell(self.start, "green")
        self.highlight_cell(self.end, "red")

    def highlight_cell(self, pos, color):
        r, c = pos
        x1 = c * self.cell_size + 2
        y1 = r * self.cell_size + 2
        x2 = x1 + self.cell_size - 4
        y2 = y1 + self.cell_size - 4
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def draw_player(self):
        if self.player_rect:
            self.canvas.delete(self.player_rect)
        self.player_rect = self.highlight_cell(self.player, "blue")

    def move_player(self, dr, dc):
        r, c = self.player
        nr, nc = r + dr, c + dc
        if 0 <= nr < self.rows and 0 <= nc < self.cols:
            if dr == -1 and (self.grid[r][c] & 8):
                self.player = (nr, nc)
            elif dr == 1 and (self.grid[r][c] & 2):
                self.player = (nr, nc)
            elif dc == -1 and (self.grid[r][c] & 4):
                self.player = (nr, nc)
            elif dc == 1 and (self.grid[r][c] & 1):
                self.player = (nr, nc)
        self.draw_player()
        if self.player == self.end:
            messagebox.showinfo("Maze Adventure", "🎉 Congratulations! You reached the end and won the game! 🎉")

# Fixed: __name__ check
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Adventure!!")
    app = MazeApp(root, rows=20, cols=20, cell_size=25)
    root.mainloop()
