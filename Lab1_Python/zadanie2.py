#algorytm bfs
# graf i sasiedzi, wybieramy z ktorego wierzcholka z ktorego zaczynamy przesukiwanie
#zbior wierzcholkow odwiedzonych i nieodwiedzonych (set- wartosci unikalne)
#dodajemy jego sasiadow do listy
#zaczynam od a, visited-true i dodaje do listy
#def funkcja (G,start,end)

from collections import deque

def zadanie2 (graph,start,end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            for neighbour in graph.get(node,[]):
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)

    return None

graph = {
'1':['2','3','5'],
'2':['1','3','4','5'],
'3':['1','2','4'],
'4':['2','3','5'],
'5':['1','2','4'],

}

print(zadanie2(graph,'1','4'))