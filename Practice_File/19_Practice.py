#실시간 그래프 그리기
'''
Entry로 입력값 받기

matplotlib과 FigureCanvasTkAgg 이용해 Tkinter 안에 그래프 표시'''

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x_data = []
y_data = []

def plot_graph():
    x = float(x_entry.get())
    y = float(y_entry.get())
    x_data.append(x)
    y_data.append(y)
    ax.clear()
    ax.plot(x_data, y_data, marker='o', linestyle='-')
    canvas.draw()

root = tk.Tk()
root.title("동적 그래프")

x_entry = tk.Entry(root)
x_entry.pack()
y_entry = tk.Entry(root)
y_entry.pack()
tk.Button(root, text="그래프 그리기", command=plot_graph).pack()

fig = Figure(figsize=(5,4))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
