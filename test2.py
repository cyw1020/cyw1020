import tkinter as tk
import random

# 游戏参数
CELL_SIZE = 30
COLS = 12
ROWS = 20
DELAY = 400

# 7种方块形状
SHAPES = [
    [(0,0), (0,1), (1,0), (1,1)],   # O
    [(0,0), (0,1), (0,2), (0,3)],   # I
    [(0,0), (1,0), (2,0), (1,1)],   # T
    [(0,0), (0,1), (1,1), (1,2)],   # S
    [(1,0), (1,1), (0,1), (0,2)],   # Z
    [(0,0), (0,1), (0,2), (1,2)],   # L
    [(1,0), (1,1), (1,2), (0,2)]    # J
]
COLORS = ["#FF6666","#66CCFF","#FFFF66","#66FF66","#FF99FF","#FFCC66","#6699FF"]

class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("俄罗斯方块")
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="#222222")
        self.canvas.pack()
        self.score_label = tk.Label(root, text="得分：0", font=("SimHei",16))
        self.score_label.pack()

        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.score = 0
        self.gameover = False
        self.new_block()
        self.bind_key()
        self.loop()

    def new_block(self):
        idx = random.randint(0, len(SHAPES)-1)
        self.block = SHAPES[idx]
        self.color = COLORS[idx]
        self.x = COLS//2 - 1
        self.y = 0
        if self.check_collision(self.x, self.y):
            self.gameover = True

    def check_collision(self, dx, dy, rotate=False):
        shape = self.rotate_shape() if rotate else self.block
        for (cx,cy) in shape:
            nx = self.x + dx + cx
            ny = self.y + dy + cy
            if nx <0 or nx >= COLS:
                return True
            if ny >= ROWS:
                return True
            if ny >=0 and self.board[ny][nx]:
                return True
        return False

    def rotate_shape(self):
        return [(-y, x) for x,y in self.block]

    def lock_block(self):
        for (cx,cy) in self.block:
            nx = self.x + cx
            ny = self.y + cy
            if ny >= 0:
                self.board[ny][nx] = self.color
        self.clear_line()
        self.new_block()

    def clear_line(self):
        clear = 0
        for r in range(ROWS-1, -1, -1):
            if all(self.board[r][c] for c in range(COLS)):
                del self.board[r]
                self.board.insert(0, [None]*COLS)
                clear +=1
        self.score += clear * 100
        self.score_label.config(text=f"得分：{self.score}")

    def draw(self):
        self.canvas.delete("all")
        # 画已经落底的方块
        for r in range(ROWS):
            for c in range(COLS):
                col = self.board[r][c]
                if col:
                    self.draw_cell(c,r,col)
        # 画当前下落方块
        for (cx,cy) in self.block:
            x = self.x + cx
            y = self.y + cy
            if y >=0:
                self.draw_cell(x,y,self.color)

    def draw_cell(self, c, r, color):
        x1 = c*CELL_SIZE
        y1 = r*CELL_SIZE
        x2 = x1+CELL_SIZE
        y2 = y1+CELL_SIZE
        self.canvas.create_rectangle(x1,y1,x2,y2,fill=color,outline="#111111")

    def move(self, dx, dy):
        if not self.check_collision(dx, dy):
            self.x += dx
            self.y += dy
            return True
        if dy>0:
            self.lock_block()
        return False

    def rotate(self):
        if not self.check_collision(0,0,rotate=True):
            self.block = self.rotate_shape()

    def drop_all(self):
        while self.move(0,1):
            pass

    def bind_key(self):
        self.root.bind("<Left>", lambda e:self.move(-1,0))
        self.root.bind("<Right>", lambda e:self.move(1,0))
        self.root.bind("<Down>", lambda e:self.move(0,1))
        self.root.bind("<Up>", lambda e:self.rotate())
        self.root.bind("<space>", lambda e:self.drop_all())

    def loop(self):
        if not self.gameover:
            self.move(0,1)
            self.draw()
            self.root.after(DELAY, self.loop)
        else:
            self.canvas.create_text(COLS*CELL_SIZE//2, ROWS*CELL_SIZE//2, fill="white", font=("SimHei",24), text="游戏结束")

if __name__ == "__main__":
    win = tk.Tk()
    game = Tetris(win)
    win.mainloop()


