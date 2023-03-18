#!/usr/bin/python3
import networkx as nx
import argparse
import random

# Set up command line argument parser
parser = argparse.ArgumentParser(description='Convert a GFA file to GraphML.')
parser.add_argument('input_file', help='Path to the input GFA file')
parser.add_argument('output_file', help='Path to the output GraphML file')

# Parse command line arguments
args = parser.parse_args()

# Read in the GFA file and create a NetworkX directed graph
g = nx.DiGraph()
map =dict()
with open(args.input_file, 'r') as f:
    for line in f:
        fields = line.strip().split('\t')
        if fields[0] == 'S':
            node_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            node_size = int(len(fields[2]))
            g.add_node(fields[1], length=node_size, color=node_color, size=node_size)
            map[fields[1]] = node_size
        elif fields[0] == 'L':
            g.add_edge(fields[1], fields[3], overlap=map[fields[1]])

# Write the graph to GraphML format
nx.write_graphml(g, args.output_file)
