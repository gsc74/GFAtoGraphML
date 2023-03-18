# GFA to GraphML Converter

This is a Python script that converts a GFA file to a GraphML file using the NetworkX library.

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

## License

This script is released under the MIT License. See `LICENSE` for more information.
