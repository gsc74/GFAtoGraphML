# GFA to GraphML Converter

This is a Python script that converts a GFA file to a GraphML file using the NetworkX library.


## Quick Start
```
git clone https://github.com/gsc74/GFAtoGraphML.git
chmod +x GFAtoGraphML.py
./GFAtoGraphML.py MHC-57b.gfa MHC-57b.graphml
```

## Requirements

- Python 3.x
- NetworkX library
- argparse library

## Usage
```
./GFAtoGraphML.py graph.gfa graph.graphml
```

- `graph.gfa`: Path to the input GFA file.
- `graph.graphml`: Path to the output GraphML file.

## Output

The script creates a directed graph where:

- Each node represents a sequence in the GFA file.
- The length of each sequence is assigned as the length of the corresponding node.
- The node color is randomly assigned.
- Each edge represents a link between two sequences in the GFA file and edge weight is equal to the sequence length of the source node.

### The resulting GraphML file can be used to visualize the graph using tools like Gephi and Graphia.

## Citation

The sample GFA file `MHC-57b.gfa` used in this script was downloaded from the [Zenodo Repository "Sample graphs and sequences for testing sequence-to-graph alignment"](https://zenodo.org/record/6617246#.ZBYQ5S8RrJM).
