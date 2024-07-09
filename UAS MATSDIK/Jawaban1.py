import heapq

def dijkstra(graph, start):
    # Inisialisasi
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    shortest_path = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path[neighbor] = current_vertex

    return distances, shortest_path

def shortest_path(graph, start, end):
    distances, paths = dijkstra(graph, start)
    route = []
    current_vertex = end
    
    while current_vertex is not None:
        route.append(current_vertex)
        current_vertex = paths[current_vertex]
        
    route.reverse()
    return route, distances[end]

# Definisikan graf sebagai dictionary
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'E': 3},
    'D': {'B': 10, 'E': 4, 'F': 11},
    'E': {'C': 3, 'D': 4, 'F': 5},
    'F': {'D': 11, 'E': 5}
}

# Temukan jalur terpendek dari A ke F
start, end = 'A', 'F'
route, distance = shortest_path(graph, start, end)

print(f"Jalur terpendek dari {start} ke {end}: {' -> '.join(route)} dengan jarak {distance}")
