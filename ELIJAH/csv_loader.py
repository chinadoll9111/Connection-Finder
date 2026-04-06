import csv

def load_csv(filename):
    graph = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            node, neighbor = row
            node = node.strip()        # ✅ FIX
            neighbor = neighbor.strip()  # ✅ FIX

            if node not in graph:
                graph[node] = []

            graph[node].append(neighbor)

    return graph