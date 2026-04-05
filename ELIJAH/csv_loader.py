import csv
def load_csv(filename):
    graph = {}
    with open(filename, 'r') as file:
        reader = csv.reader
        next(reader)

        for row in reader:
            node, neighbour = row 

            if node not in graph:
                graph[node] = []

                graph[node].append(neighbour)
    return graph            