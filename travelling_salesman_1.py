import random
from sys import maxsize
from itertools import permutations

v = 4


def travellingSalesmanProblem(graph, starting_city):
    vertex = []
    for i in range(0,v):
        if i != starting_city:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    route = []
    for perm in next_permutation:
        current_pathweight = 0
        k = starting_city
        for city in perm:
            current_pathweight += graph[k][city]
            k = city
        current_pathweight += graph[k][starting_city]
        if current_pathweight < min_path:
            min_path = current_pathweight
            route = list(perm)
        min_path = min(min_path, current_pathweight)
        # route = list(perm)
    route = [starting_city,]+route+[starting_city,]
    return min_path, route


if __name__ == "__main__":
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    s = 0
    cost, path = travellingSalesmanProblem(graph, s)
    print("Min cost is: ", cost)
    print("Shortest route is: ", path)