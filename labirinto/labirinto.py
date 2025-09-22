import graphviz

def plot_tree_from_file(filename, output_filename="tree"):
    """
    Read a tree structure from a text file and plot it using Graphviz
    
    Args:
        filename (str): Path to the input text file
        output_filename (str): Base name for the output image file
    """
    
    # Create a new directed graph
    dot = graphviz.Digraph(comment='Tree Structure')
    
    # Read the file and process each line
    with open(filename, 'r') as file:
        for line in file:
            # Remove whitespace and split into parent and child nodes
            line = line.strip()
            if not line:  # Skip empty lines
                continue
                
            parent, child = line.split()
            
            # Add nodes and edge to the graph
            dot.node(parent, parent)
            dot.node(child, child)
            dot.edge(parent, child)
    
    # Render the graph to an image file
    dot.render(output_filename, format='png', cleanup=True)
    print(f"Tree plot saved as {output_filename}.png")

# Example usage
if __name__ == "__main__":
    # Create a sample input file with your data
    
    # Plot the tree
    plot_tree_from_file('example.txt', 'tree_plot')
    
    # Alternatively, use your own file:
    # plot_tree_from_file('your_tree_file.txt', 'my_tree')