import graphviz
import subprocess
import os

def plot_colored_graph_from_file(filename):
    """
    Read a graph structure and node colors from a text file and plot it using Graphviz
    
    Args:
        filename (str): Path to the input text file
        output_filename (str): Base name for the output image file
    """
    
    # Create a new undirected graph
    dot = graphviz.Graph(comment='Colored Graph')
    
    # Read the entire file
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    # Separate edges from node colors info
    edges = []
    color_data = []
    num_nodes = 0
    num_colors = 0
    found_color_info = False
    
    for line in lines:
        if "num of nodes:" in line and "num of colors" in line:
            parts = line.split()
            # Find the positions of numbers
            for i, part in enumerate(parts):
                if part == "nodes:" and i + 1 < len(parts):
                    num_nodes = int(parts[i + 1])
                if part == "colors" and i + 1 < len(parts):
                    num_colors = int(parts[i + 1])
            found_color_info = True
        elif found_color_info:
            # After finding color info, the rest are color values
            color_data.append(int(line))
        else:
            # Before finding color info, these are edges
            if len(line.split()) == 2:
                edges.append(line)
    
    # Create color palette
    color_palette = [
        '#FF6B6B', "#2BFF00", "#4566D1", "#00FF88", '#FFEAA7',
        '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9',
        '#F8C471', '#82E0AA', '#F1948A', '#85C1E9', '#D7BDE2',
        '#F9E79F', '#A9DFBF', '#F5B7B1', '#D2B4DE', '#AED6F1'
    ]
    
    # If we need more colors than available in palette, generate them
    if num_colors > len(color_palette):
        import colorsys
        color_palette = []
        for j in range(num_colors):
            hue = j / num_colors
            rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
            hex_color = '#{:02x}{:02x}{:02x}'.format(
                int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
            )
            color_palette.append(hex_color)
    
    # Process edges and add nodes with colors
    node_colors = {}
    edge_set = set()
    
    for edge_line in edges:
        parent, child = edge_line.split()
        
        # Create both possible edge representations
        edge_forward = (parent, child)
        edge_reverse = (child, parent)
        
        # Check if edge or its reverse already exists
        if edge_forward not in edge_set and edge_reverse not in edge_set:
            # Add to edge set
            edge_set.add(edge_forward)
            
            # Add parent node with color if not already added
            if parent not in node_colors:
                color_idx = color_data[int(parent)]
                dot.node(parent, parent, style='filled', fillcolor=color_palette[color_idx])
                node_colors[parent] = color_palette[color_idx]
            
            # Add child node with color if not already added
            if child not in node_colors:
                color_idx = color_data[int(child)]
                dot.node(child, child, style='filled', fillcolor=color_palette[color_idx])
                node_colors[child] = color_palette[color_idx]
            
            # Add edge to graph (undirected)
            dot.edge(parent, child)
    
    # Add any remaining nodes that might not be in edges but have colors
    for node_id in range(num_nodes):
        node_str = str(node_id)
        if node_str not in node_colors and node_id < len(color_data):
            color_idx = color_data[node_id]
            dot.node(node_str, node_str, style='filled', fillcolor=color_palette[color_idx])
    
    # Render the graph to an image file
    output_filename = str.split(filename,'.')[0] + "_colored"
    dot.render(output_filename, format='png', cleanup=True)
    print(f"Colored graph plot saved as {output_filename}.png")

# Usage
if __name__ == "__main__":
    filename = None
    while filename is None:
        print("Backtrack ou Greedy (b/g):")
        res = input().strip().lower()

        if res == 'b':
            # roda o backtrack em Python
            subprocess.run(["python3", "backtrack.py"])
            filename = "resultado_backtrack.txt"

        elif res == 'g':
            # compila e roda o greedy em C++
            subprocess.run(["g++", "greedy.cpp", "-o", "greedy_exec"])
            subprocess.run(["./greedy_exec"])
            filename = "resultado_greedy.txt"

    # depois de rodar, chama o plot
    plot_colored_graph_from_file(filename)