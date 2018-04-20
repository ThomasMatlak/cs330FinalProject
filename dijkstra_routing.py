#!/usr/bin/python3

'''
Network routing with Dijkstra's algorithm
'''


import math

# TODO be able to run for one node
# TODO be able to run for all nodes

import sys
import queue

def parse_graph_file(filename):
    ''' 
    The first line of an input file is the number of vertices, v
    The second line is the number of edges, e
    The next e lines contain pairs of adjacent vertices
    '''
    vertices = []
    edges = []
    with open(filename, 'r') as infile:
        n_vertices = int(infile.readline())
        n_edges = int(infile.readline())

        for _ in range(n_edges):
            edges.append(tuple(int(v.strip()) for v in infile.readline().split()))

    vertices = [v for v in range(n_vertices)]

    return vertices, edges


def dijkstra(src, vertices, edges):
    dist = [(v, math.inf) for v in vertices]
    prev = [None for _ in vertices]

    dist[src] = (src, 0)

    Q = []
    for v in vertices:
        Q.append(v)

    while len(Q) > 0:
        u = sorted(dist, key=lambda v: v[1])[len(vertices) - len(Q)][0]
        Q.remove(u)

        for e in edges:
            if u == e[0]:
                v = e[1]
            elif u == e[1]:
                v = e[0]
            else:
                continue

            alt = dist[u][1] + 1  # if using a weighted graph, change from 1 to the edge weight
            if alt < dist[v][1]:
                dist[v] = (v, alt)
                prev[v] = u

    return dist, prev


def main():
    vertices, edges = parse_graph_file("default_graph.txt")

    dist, prev = dijkstra(0, vertices, edges)

    print(dist)
    print(prev)


if __name__ == '__main__':
    main()
