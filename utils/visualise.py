import json
from pyvis.network import Network

# Load the JSON data
with open('available.json', 'r') as file:
    data = json.load(file)

# Initialize a network
net = Network(directed=True)


# Process each entry in the JSON data
for entry in data:
    input_node = f"{entry['input_model']} {entry['input_version']}"
    output_node = f"{entry['output_model']} {entry['output_version']}"

    # Add nodes to the set
    net.add_node(input_node)
    net.add_node(output_node)

    # Add edge from input to output
    net.add_edge(input_node, output_node)


# Generate the network map and save it to an HTML file
net.show('network_map.html', notebook=False)
