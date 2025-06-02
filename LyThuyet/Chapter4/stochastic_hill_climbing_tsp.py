import math
import random
# import matplotlib.pyplot as plt


class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance_to(self, other_city):
        return math.sqrt((self.x - other_city.x)**2 + (self.y - other_city.y)**2)

    def __repr__(self):
        return self.name



def create_romania_map():
    """Creates a dictionary representing the Romania map with distances."""
    cities = {
        "Arad": City("Arad", 91, 492),
        "Zerind": City("Zerind", 108, 531),
        "Oradea": City("Oradea", 129, 573),
        "Timisoara": City("Timisoara", 73, 410),
        "Lugoj": City("Lugoj", 160, 370),
        "Mehadia": City("Mehadia", 177, 335),
        "Drobeta": City("Drobeta", 189, 298),
        "Sibiu": City("Sibiu", 226, 466),
        "Rimnicu": City("Rimnicu", 230, 411),
        "Craiova": City("Craiova", 275, 280),
        "Fagaras": City("Fagaras", 310, 480),
        "Pitesti": City("Pitesti", 321, 370),
        "Bucharest": City("Bucharest", 408, 323),
        "Giurgiu": City("Giurgiu", 397, 259),
        "Urziceni": City("Urziceni", 489, 334),
        "Neamt": City("Neamt", 450, 540),
        "Iasi": City("Iasi", 505, 497),
        "Vaslui": City("Vaslui", 532, 444),
        "Hirsova": City("Hirsova", 588, 334),
        "Eforie": City("Eforie", 598, 263)
    }

    distances = {
        ("Arad", "Zerind"): 75,
        ("Arad", "Sibiu"): 140,
        ("Arad", "Timisoara"): 118,
        ("Zerind", "Oradea"): 71,
        ("Oradea", "Sibiu"): 151,
        ("Timisoara", "Lugoj"): 111,
        ("Lugoj", "Mehadia"): 70,
        ("Mehadia", "Drobeta"): 75,
        ("Drobeta", "Craiova"): 120,
        ("Sibiu", "Fagaras"): 99,
        ("Sibiu", "Rimnicu"): 80,
        ("Rimnicu", "Craiova"): 146,
        ("Rimnicu", "Pitesti"): 97,
        ("Craiova", "Pitesti"): 138,
        ("Fagaras", "Bucharest"): 211,
        ("Pitesti", "Bucharest"): 101,
        ("Bucharest", "Giurgiu"): 90,
        ("Bucharest", "Urziceni"): 85,
        ("Urziceni", "Hirsova"): 98,
        ("Urziceni", "Vaslui"): 142,
        ("Neamt", "Iasi"): 87,
        ("Iasi", "Vaslui"): 92,
        ("Hirsova", "Eforie"): 86
    }
    return cities, distances


def calculate_total_distance(route, cities, distances):
    """Calculates the total distance of a given route."""
    total_distance = 0
    for i in range(len(route) - 1):
        city1_name = route[i]
        city2_name = route[i + 1]

       
        if (city1_name, city2_name) in distances:
          total_distance += distances[(city1_name, city2_name)]
        elif (city2_name, city1_name) in distances:
          total_distance += distances[(city2_name, city1_name)]
        else:
          
            city1 = cities[city1_name]
            city2 = cities[city2_name]
            total_distance += city1.distance_to(city2) 
    
    
    if (route[-1], route[0]) in distances:
       total_distance+= distances[(route[-1], route[0])]
    elif (route[0], route[-1]) in distances:
        total_distance+= distances[(route[0], route[-1])]
    else:
        city1 = cities[route[-1]]
        city2 = cities[route[0]]
        total_distance += city1.distance_to(city2)


    return total_distance


def get_neighbor(route, tabu_list=set()):
    """Sinh hàng xóm bằng cách hoán đổi hai thành phố, tránh lặp lại."""
    neighbor = route[:]
    
    while True:
        idx1, idx2 = random.sample(range(len(route)), 2)

        # Kiểm tra nếu hoán đổi này đã từng xảy ra gần đây
        if (idx1, idx2) not in tabu_list and (idx2, idx1) not in tabu_list:
            break  # Nếu hợp lệ thì thoát vòng lặp
    
    # Thực hiện hoán đổi
    neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]

    # Cập nhật Tabu List (giữ tối đa 10 phần tử)
    tabu_list.add((idx1, idx2))
    if len(tabu_list) > 10:
        tabu_list.pop()

    return neighbor

def stochastic_hill_climbing(cities, distances, max_iterations=1000, num_restarts=10):
    """Implements the stochastic hill climbing algorithm."""

    best_route = None
    best_distance = float('inf')

    for _ in range(num_restarts):
        
        current_route = list(cities.keys())
        random.shuffle(current_route)
        current_distance = calculate_total_distance(current_route, cities, distances)


        for _ in range(max_iterations):
            neighbor = get_neighbor(current_route)
            neighbor_distance = calculate_total_distance(neighbor, cities, distances)

            if neighbor_distance < current_distance:  
                current_route = neighbor
                current_distance = neighbor_distance
            else:                                  
                delta = neighbor_distance - current_distance
                acceptance_probability = math.exp(-delta)  
                if random.random() < acceptance_probability:
                    current_route = neighbor
                    current_distance = neighbor_distance

        if current_distance < best_distance:  
            best_distance = current_distance
            best_route = current_route

    return best_route, best_distance


def plot_route(route, cities, title="TSP Route"):
    """Plots the given route on a map."""
    x_coords = [cities[city].x for city in route]
    y_coords = [cities[city].y for city in route]

    
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])

    # plt.figure(figsize=(10, 8)) 
    # plt.plot(x_coords, y_coords, 'o-', label="Route")
    # plt.scatter(x_coords, y_coords, s=50) 
 
    for i, city_name in enumerate(route):
      plt.annotate(city_name, (x_coords[i], y_coords[i]), textcoords="offset points", xytext=(5,5), ha='left')


    # plt.title(title)
    # plt.xlabel("X Coordinate")
    # plt.ylabel("Y Coordinate")
    # plt.grid(True)
    # plt.show()


if __name__ == "__main__":
    cities, distances = create_romania_map()
    best_route, best_distance = stochastic_hill_climbing(cities, distances, max_iterations=5000, num_restarts=20) 

    print("Best route:")
    for value in best_route:
        print(value, end=" -> ")
    print(best_route[0])
    print("Total distance:", best_distance)
    # plot_route(best_route, cities, title=f"TSP Route (Distance: {best_distance:.2f})")