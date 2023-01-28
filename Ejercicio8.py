class Planet:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = {}
        self.min_distance = float("inf")
        self.previous = None
    
    def add_neighbor(self, planet, distance):
        self.neighbors.append(planet)
        self.distance[planet] = distance

def prim(graph, start_planet):
    included_planets = set()
    tree_edges = []
    included_planets.add(start_planet)
    while len(included_planets) < len(graph):
        min_edge_weight = float("inf")
        min_edge = None
        for planet in included_planets:
            for neighbor in planet.neighbors:
                if neighbor not in included_planets:
                    if planet.distance[neighbor] < min_edge_weight:
                        min_edge_weight = planet.distance[neighbor]
                        min_edge = (planet, neighbor)
        included_planets.add(min_edge[1])
        tree_edges.append(min_edge)
    return tree_edges

def dijkstra(graph, start_planet, end_planet):
    for planet in graph:
        planet.min_distance = float("inf")
    start_planet.min_distance = 0
    unvisited_planets = list(graph)
    while unvisited_planets:
        current_planet = min(unvisited_planets, key=lambda x: x.min_distance)
        if current_planet == end_planet:
            break
        unvisited_planets.remove(current_planet)
        for neighbor in current_planet.neighbors:
            if neighbor in unvisited_planets:
                distance = current_planet.distance[neighbor]
                if current_planet.min_distance + distance < neighbor.min_distance:
                    neighbor.min_distance = current_planet.min_distance + distance
                    neighbor.previous = current_planet
    path = []
    planet = end_planet
    while planet:
        path.append(planet)
        planet = planet.previous
    path.reverse()
    return path

def bfs(graph, start_planet):
    visited_planets = set()
    queue = [start_planet]
    visited_planets.add(start_planet)
    while queue:
        current_planet = queue.pop(0)
        for neighbor in current_planet.neighbors:
            if neighbor not in visited_planets:
                visited_planets.add(neighbor)
                queue.append(neighbor)
    return visited_planets

# Crear los objetos de la clase "Planet" y establecer las conexiones entre ellos
Tierra = Planet("Tierra")
Knowhere = Planet("Knowhere")
ZenWhoberi = Planet("Zen-Whoberi")
Vormir = Planet("Vormir")
Titan = Planet("Titan")
Nidavellir = Planet("Nidavellir")
planet1 = Planet("planet1")
planet2 = Planet("planet2")
planet3 = Planet("planet3")
planet4 = Planet("planet4")
planet5 = Planet("planet5")
planet6 = Planet("planet6")
planet7 = Planet("planet7")

Tierra.add_neighbor(Knowhere, 20)
Tierra.add_neighbor(ZenWhoberi, 25)
Tierra.add_neighbor(Vormir, 30)
Tierra.add_neighbor(Titan, 25)

Knowhere.add_neighbor(Tierra, 20)
Knowhere.add_neighbor(ZenWhoberi, 15)
Knowhere.add_neighbor(Vormir, 20)
Knowhere.add_neighbor(Titan, 25)

ZenWhoberi.add_neighbor(Tierra, 25)
ZenWhoberi.add_neighbor(Knowhere, 15)
ZenWhoberi.add_neighbor(Vormir, 25)
ZenWhoberi.add_neighbor(Titan, 30)

Vormir.add_neighbor(Tierra, 30)
Vormir.add_neighbor(Knowhere, 20)
Vormir.add_neighbor(ZenWhoberi, 25)
Vormir.add_neighbor(Titan, 20)

Titan.add_neighbor(ZenWhoberi, 30)
Titan.add_neighbor(Vormir, 20)
Titan.add_neighbor(Nidavellir, 20)
Titan.add_neighbor(Tierra, 25)

Nidavellir.add_neighbor(Titan, 20)
Nidavellir.add_neighbor(Tierra, 20)
Nidavellir.add_neighbor(Vormir, 30)
Nidavellir.add_neighbor(ZenWhoberi, 30)

planet1.add_neighbor(Nidavellir, 20)
planet1.add_neighbor(planet2, 20)
planet1.add_neighbor(planet3, 25)
planet1.add_neighbor(planet4, 30)

planet2.add_neighbor(Vormir, 25)
planet2.add_neighbor(planet1, 20)
planet2.add_neighbor(planet3, 20)
planet2.add_neighbor(planet4, 30)

planet3.add_neighbor(planet1, 25)
planet3.add_neighbor(planet2, 20)
planet3.add_neighbor(planet5, 20)
planet3.add_neighbor(planet6, 30)

planet4.add_neighbor(planet2, 30)
planet4.add_neighbor(planet5, 25)
planet4.add_neighbor(planet6, 20)
planet4.add_neighbor(planet7, 30)

planet5.add_neighbor(planet3, 20)
planet5.add_neighbor(planet4, 25)
planet5.add_neighbor(planet7, 30)
planet5.add_neighbor(planet6, 20)

planet6.add_neighbor(planet4, 20)
planet6.add_neighbor(planet7, 25)
planet6.add_neighbor(planet5, 20)
planet6.add_neighbor(planet3, 30)

planet7.add_neighbor(planet5, 30)
planet7.add_neighbor(planet6, 25)
planet7.add_neighbor(planet4, 30)
planet7.add_neighbor(planet2, 20)


graph = [Tierra, Knowhere, ZenWhoberi, Vormir, Titan, Nidavellir, planet1, planet2, planet3, planet4, planet5, planet6, planet7]

# Crear el árbol de expansión mínima
tree = prim(graph, Tierra)
print("Árbol de expansión mínima:")
for edge in tree:
    print(f"{edge[0].name} -> {edge[1].name}")

# Encontrar el camino más corto desde Zen-Whoberi hasta Nidavellir
path = dijkstra(graph, ZenWhoberi, Nidavellir)
print("\nCamino más corto desde Zen-Whoberi hasta Nidavellir:")
for planet in path:
    print(planet.name)

# Encontrar el camino más corto desde Tierra hasta Vormir
path = dijkstra(graph, Tierra, Vormir)
print("\nCamino más corto desde Tierra hasta Vormir:")
for planet in path:
    print(planet.name)

# Encontrar el camino más corto desde Knowhere hasta Titan
path = dijkstra(graph, Knowhere, Titan)
print("\nCamino más corto desde Knowhere hasta Titan:")
for planet in path:
    print(planet.name)

#Determinar todos los planetas a los que se puede llegar desde Titan
reachable_planets = bfs(graph, Titan)
print("\nPlanetas a los que se puede llegar desde Titan:")
for planet in reachable_planets:
    print(planet.name)