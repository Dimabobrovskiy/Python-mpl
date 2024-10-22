import matplotlib.pyplot as plt

#чтениe данных из файла
def read_data(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        # Чтение числа точек
        n = int(f.readline().strip())
        
        # Чтение координат точек
        points = []
        for _ in range(n):
            x, y = map(float, f.readline().strip().split())
            points.append((x, y))
    
    return points

#визуализациz данных с масштабированием через plt.axis('scaled')
def plot_data(points):

    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    
    
    plt.scatter(x_values, y_values)
    
    
    plt.title(f"Number of points: {len(points)}")
    
    
    plt.axis('scaled')
    
    
    plt.savefig('005.png')
    plt.show()

file_path = r"C:\Users\dimab\OneDrive\Desktop\lab1\005.dat"  # Путь к файлу с данными
points = read_data(file_path)
plot_data(points)

