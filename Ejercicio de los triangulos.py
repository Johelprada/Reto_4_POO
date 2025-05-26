# Clase para representar un punto en el plano
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def compute_distance(self, other):
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y


# Clase para representar una línea entre dos puntos
class Line:
    def __init__(self, start_point, end_point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)

    def get_start_point(self):
        return self._start_point

    def get_end_point(self):
        return self._end_point

    def get_length(self):
        return self._length

    def set_start_point(self, p):
        self._start_point = p
        self._length = self._start_point.compute_distance(self._end_point)

    def set_end_point(self, p):
        self._end_point = p
        self._length = self._start_point.compute_distance(self._end_point)


# Clase base para cualquier figura
class Shape:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = self._compute_edges()
        self._inner_angles = []
        self._is_regular = False

    def _compute_edges(self):
        print("\nlíneas que forman la figura...")
        edges = []
        for i in range(len(self._vertices)):
            start = self._vertices[i]
            end = self._vertices[(i + 1) % len(self._vertices)]
            line = Line(start, end)
            print(f"  Lado {i+1} de longitud {line.get_length():.2f}")
            edges.append(line)
        return edges

    def compute_perimeter(self):
        perimeter = sum(edge.get_length() for edge in self._edges)
        print(f"  Perímetro total: {perimeter:.2f}")
        return perimeter

    def compute_area(self):
        raise NotImplementedError("Área no implementada para figura genérica")

    def compute_inner_angles(self):
        raise NotImplementedError("Ángulos internos no implementados")

    def get_edges(self):
        return self._edges

    def get_vertices(self):
        return self._vertices

    def get_is_regular(self):
        return self._is_regular


# Clase para representar un rectángulo
class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._is_regular = False

    def compute_area(self):
        l1 = self._edges[0].get_length()
        l2 = self._edges[1].get_length()
        area = l1 * l2
        print(f"  Área = {l1:.2f} x {l2:.2f} = {area:.2f}")
        return area


# Clase cuadrado que hereda de rectángulo
class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._is_regular = True


# Clase base para triángulos
class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)

    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self._edges]
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"  Lados: {a:.2f}, {b:.2f}, {c:.2f}")
        print(f"  Semiperímetro: {s:.2f}")
        print(f"  Área: {area:.2f}")
        return area


class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._is_regular = True


class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


class TriRectangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


# Menu para porbar
if __name__ == "__main__":
    print("Bienvenido al sistema de figuras geométricas :)\n")
    print("1. Crear un cuadrado")
    print("2. Crear un rectángulo")
    print("3. Crear un triángulo escaleno")
    opcion = input("¿Qué figura quieres probar? (1/2/3): ")

    if opcion == '1':
        # Cuadrado de lado 2
        p1 = Point(0, 0)
        p2 = Point(0, 2)
        p3 = Point(2, 2)
        p4 = Point(2, 0)
        figura = Square([p1, p2, p3, p4])

    elif opcion == '2':
        # Rectángulo 3x2
        p1 = Point(0, 0)
        p2 = Point(0, 3)
        p3 = Point(2, 3)
        p4 = Point(2, 0)
        figura = Rectangle([p1, p2, p3, p4])

    elif opcion == '3':
        # Triángulo escaleno
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(2, 3)
        figura = Scalene([p1, p2, p3])

    else:
        print("Opción no válida")
        exit()


    figura.compute_perimeter()
    figura.compute_area()
    print(f"¿Es regular? {'Sí' if figura.get_is_regular() else 'No'}")
