import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

class VoronoiDiagram:
    def __init__(self, width, height, num_seeds):
        """
        Initialize the Voronoi diagram generator.
        
        Args:
            width (int): Width of the diagram in pixels.
            height (int): Height of the diagram in pixels.
            num_seeds (int): Number of seed points (Voronoi sites).
        """
        self.width = width
        self.height = height
        self.num_seeds = num_seeds
        self.seeds = None
        self.diagram = None
    
    def generate_seeds(self):
        """Generate random seed points within the diagram boundaries."""
        x = np.random.uniform(0, self.width, self.num_seeds)
        y = np.random.uniform(0, self.height, self.num_seeds)
        self.seeds = np.column_stack((x, y))
        return self.seeds
    
    def generate(self):
        """Generate the Voronoi diagram using KDTree for nearest-neighbor search."""
        if self.seeds is None:
            self.generate_seeds()
        
        # Build KDTree for efficient distance queries
        tree = KDTree(self.seeds)
        
        # Create grid of coordinates for every pixel in the diagram
        x_coords = np.arange(self.width)
        y_coords = np.arange(self.height)
        grid_x, grid_y = np.meshgrid(x_coords, y_coords)
        pixel_coords = np.column_stack((grid_x.ravel(), grid_y.ravel()))
        
        # Query nearest seeds for all pixels
        _, indices = tree.query(pixel_coords)
        
        # Reshape into 2D diagram
        self.diagram = indices.reshape((self.height, self.width))
        return self.diagram
    
    def plot(self, show_seeds=True):
        """Plot the Voronoi diagram using matplotlib. Used for debugging."""
        if self.diagram is None:
            self.generate()
        
        plt.figure(figsize=(10, 8))
        plt.imshow(self.diagram, cmap='viridis', origin='lower', 
                   extent=[0, self.width, 0, self.height])
        
        if show_seeds:
            plt.scatter(self.seeds[:, 0], self.seeds[:, 1], 
                        c='red', s=20, marker='x', label='Seeds')
            plt.legend()
        
        plt.title('Voronoi Diagram')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

# Example usage
if __name__ == "__main__":
    voronoi = VoronoiDiagram(1000, 1000, 50)
    voronoi.generate()
    voronoi.plot()
