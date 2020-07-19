# punkter med koordinater (x, y) med label s={A, B, C, D...}.
# I en cirkel från origo, vad är maximala antalet punkter som får plats
# Om det bara får vara en label av varje typ.
import random
import math

def generate_test_case(length, label):
    X = [random.randint(0, 50) for _ in range(length)]
    Y = [random.randint(0, 50) for _ in range(length)]
    S = [random.choice(label) for _ in range(length)]

    return (X, Y, S)

X, Y, S = generate_test_case(10, ['A', 'B', 'C', 'D'])

class Point:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        self.calc_dist()

    def calc_dist(self):
        self.dist = math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.s})"

def solution(X, Y, S):
    points = [Point(x, y, s) for x, y, s in zip(X, Y, S)]
    sorted_points = sorted(points, key=lambda p: p.dist)

    circle = [sorted_points[0]]
    for new_point in sorted_points:
        # Check all current labels already in circle
        # If label already in circle, check distance to previous, if same, remove both.
        current_labels = [point.s for point in circle]
        if new_point.s in current_labels:
            if circle[-1].dist == new_point.dist:
                circle.pop()
        else:
            circle.append(new_point)
    return circle


if __name__ == "__main__":
    sol = solution(X, Y, S)
    print(sol)