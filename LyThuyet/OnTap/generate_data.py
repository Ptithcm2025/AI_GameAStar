import random
def generate_test_data():
    # Danh sách cạnh (đỉnh 1, đỉnh 2)
    edges = [
        (1, 2), (1, 3), (1, 4),
        (2, 5), (2, 6),
        (4, 7), (4, 8), (4, 9),
        (6, 10), (6, 11),
        (7, 11), (8, 12), (8, 13),
        (9, 13), (9, 14)
    ]

    # Thêm khoảng cách ngẫu nhiên cho mỗi cạnh
    weighted_edges = [(u, v, random.randint(1, 100)) for u, v in edges]

    # Số đỉnh và số cạnh
    num_vertices = 15
    num_edges = len(weighted_edges)

    return num_vertices, num_edges, weighted_edges

def print_test_data(num_vertices, num_edges, weighted_edges):
    print(f"{num_vertices} {num_edges}")
    for u, v, weight in weighted_edges:
        print(f"{u} {v} {weight}")