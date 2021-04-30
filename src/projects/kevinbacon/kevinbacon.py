#!/usr/bin/env python3
"""
`kevinbacon` implementation

@authors: Adam Mertzenich
@version: 2021.4
"""

import sys
from typing import List

from pythonds3.graphs import Graph


def read_file(filename: str) -> Graph:
    """Build a graph from the file"""
    graph = Graph()

    combo: dict = {}
    with open(filename, "r") as file:
        content = file.readlines()
        for i in content[1:]:
            val = i.strip().split("|")
            if val[0] not in combo:
                combo[val[0]] = []
            combo[val[0]].append(val[1])

    for movie in combo:
        for actor in combo[movie]:
            for loc in range(len(combo[movie])):
                if actor != combo[movie][loc]:
                    graph.add_edge(actor, combo[movie][loc], 1)
    return graph


def traverse(graph, src, dst):
    """Traverse a graph"""
    path = []
    current = graph.get_vertex(dst)
    while current:
        path.append(current)
        current = current.previous
    return graph.get_vertex(dst).distance


def find_max_kbn_actors(graph: Graph) -> List[str]:
    """Find actor(s) with the highest KBN value"""
    key: list = []
    val: list = []
    for i in graph.get_vertices():
        if len(key) == 0:
            key.append(i)
            val.append(traverse(graph, "Kevin Bacon", i))
        else:
            trav = traverse(graph, "Kevin Bacon", i)
            if sys.maxsize > trav > val[-1]:
                key.clear()
                val.clear()
                key.append(i)
                val.append(traverse(graph, "Kevin Bacon", i))
            if trav == val[-1] and trav < sys.maxsize and i not in key:
                key.append(i)
                val.append(traverse(graph, "Kevin Bacon", i))
    return key


def main():
    """Main function"""
    print("Initializing...", "\n")

    the_graph = read_file("data/projects/kevinbacon/movie_actors_full.txt")
    the_graph.bfs(the_graph.get_vertex("Kevin Bacon"))
    while True:
        question = input("What actor would you like to trace (exit to quit) ")
        if question == "exit":
            break
        try:
            if traverse(the_graph, "Kevin Bacon", question) == sys.maxsize:
                print("No connection found.")
            else:
                print(
                    f"{question}'s Kevin Bacon number is",
                    traverse(the_graph, "Kevin Bacon", question)
                )
                road_to_kb = []
                vertex = the_graph.get_vertex(question)
                while vertex:
                    road_to_kb.append(vertex.key)
                    vertex = vertex.previous
                print("Path: ", " -> ".join(road_to_kb), "\n")
        except AttributeError:
            print("No connection found.")


if __name__ == "__main__":
    main()
