#실시간 그래프 그리기
'''
x, y 입력값을 받아 그래프에 점을 추가하시오.
'''

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x_data, y_data = [], []

def plot_graph():
    x = float(x_entry.get())
    y = float(y_entry.get())
    x_data.append(x)
    y_data.append(y)
    ax.clear()
    ax.plot(x_data, y_data, marker='o')
    canvas.draw()

root = tk.Tk()
x_entry = tk.Entry(root); x_entry.pack()
y_entry = tk.Entry(root); y_entry.pack()
tk.Button(root, text="그래프 추가", command=plot_graph).pack()

fig = Figure(figsize=(5,4))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
