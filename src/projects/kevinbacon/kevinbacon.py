#!/usr/bin/env python3
"""
`kevinbacon` implementation

@authors: Adam Mertzenich
@version: 2021.4
"""

import sys
import argparse
import time
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
                    graph.add_edge(actor, combo[movie][loc])
    return graph


def find_max_kbn_actors(graph: Graph) -> List[str]:
    """Find actor(s) with the highest KBN value"""
    raise NotImplementedError


def main():
    """Main function"""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("actor", type=str, nargs="*")
    args = argparser.parse_args()

    print("Kevin Bacon number calculator")
    print("Reading the file")
    the_graph = read_file("/home/adam/Documents/CS-160/ads-class-pub/data/projects/kevinbacon/movie_actors_full.txt")

    print("Analyzing the graph")
    connections = 0
    for vertex in the_graph:
        connections = connections + len(vertex.get_neighbors())
    print(f"There are {len(the_graph)} connected actors in the file")
    print(f"There are {connections} connections between actors in the file")
    print()

    # print("Finding paths")
    # kevin = the_graph.get_vertex("Kevin Bacon")
    # time_start = time.time()
    # the_graph.bfs(kevin)
    # time_end = time.time()
    # elapsed = time_end - time_start
    # print(f"Paths found in {elapsed:.2f} sec")
    # print()

    # print("Looking for actors with the highest Kevin Bacon number")
    # time_start = time.time()
    # high_kbn_lst = find_max_kbn_actors(the_graph)
    # time_end = time.time()
    # elapsed = time_end - time_start
    # print(f"{len(high_kbn_lst)} actor(s) found in {elapsed:.2f} sec")
    # print(
    #     "The following actor(s) have the Kevin Bacon number of "
    #     + f"{the_graph.get_vertex(high_kbn_lst[0]).get_distance()}:"
    # )
    # for name in high_kbn_lst:
    #     print(name)
    # print()

    # actor = " ".join(args.actor) or high_kbn_lst[0]
    # raise NotImplementedError


if __name__ == "__main__":
    main()
