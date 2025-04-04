class Point:
    def __init__(self, coordinate_x, coordinate_y, color="black"):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.color = color

if __name__ == "__main__":

    points = [Point(0, 0, "red") for _ in range(1000)]
    print("Кількість точок:", len(points))

    points[2].coordinate_x = 10
    print("Значення координати x третьої точки:", points[2].coordinate_x)
