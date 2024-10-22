import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

#чтение данных из файла
def read_data(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    
    
    frames = []
    for i in range(0, len(lines), 2):
        x_values = list(map(float, lines[i].strip().split()))
        y_values = list(map(float, lines[i + 1].strip().split()))
        frames.append((x_values, y_values))
    
    return frames

#создание гифки
def animate_frames(frames, output_gif):
    
    all_x = [x for frame in frames for x in frame[0]]
    all_y = [y for frame in frames for y in frame[1]]
    
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid(True)

    
    line, = ax.plot([], [], lw=2)

    
    def update(frame_data):
        x_values, y_values = frame_data
        line.set_data(x_values, y_values)
        ax.set_title(f"Frame {frames.index(frame_data)}")
        return line,

   
    anim = FuncAnimation(fig, update, frames=frames, blit=True)

    
    anim.save(output_gif, writer=PillowWriter(fps=2))
    plt.close()


file_path = r"C:\Users\dimab\OneDrive\Desktop\Second\Frames.dat"  # Путь к  файлу с данными
output_gif = r"C:\Users\dimab\OneDrive\Desktop\Second\animation.gif"  # Путь для сохранения GIF

frames = read_data(file_path)
animate_frames(frames, output_gif)
