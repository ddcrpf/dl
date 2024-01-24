print("""
import numpy as np
import matplotlib.pyplot as plt

class KohonenSOM:
    def __init__(self, input_size, map_size):
        self.input_size = input_size
        self.map_size = map_size
        self.weights = np.random.rand(map_size[0], map_size[1], input_size)

    def update_weights(self, input_vector, winner, learning_rate, neighborhood_radius):
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                weight_vector = self.weights[i, j, :]
                distance = np.linalg.norm(np.array([i, j]) - np.array(winner))
                influence = np.exp(-(distance*2) / (2 * neighborhood_radius*2))
                self.weights[i, j, :] += learning_rate * influence * (input_vector - weight_vector)

    def train(self, data, epochs, initial_learning_rate=0.1, initial_radius=None):
        if initial_radius is None:
            initial_radius = max(self.map_size) / 2

        for epoch in range(epochs):
            learning_rate = initial_learning_rate * np.exp(-epoch / epochs)
            neighborhood_radius = initial_radius * np.exp(-epoch / epochs)

            for input_vector in data:
                winner = self.find_winner(input_vector)
                self.update_weights(input_vector, winner, learning_rate, neighborhood_radius)

    def find_winner(self, input_vector):
        min_distance = float('inf')
        winner = (0, 0)

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                weight_vector = self.weights[i, j, :]
                distance = np.linalg.norm(input_vector - weight_vector)

                if distance < min_distance:
                    min_distance = distance
                    winner = (i, j)

        return winner

    def visualize(self, data):
        colors = ['r', 'g', 'b', 'y', 'c', 'm']

        for input_vector in data:
            winner = self.find_winner(input_vector)
            plt.scatter(winner[0], winner[1], color=colors[np.random.randint(len(colors))])

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                plt.scatter(i, j, color='k', marker='x')

        plt.show()

# Example usage:
if __name__ == "__main__":
    # Generate some random 2D data points
    data = np.random.rand(100, 2)

    # Create a Kohonen SOM with input size 2 and a 10x10 map
    som = KohonenSOM(input_size=2, map_size=(10, 10))

    # Train the SOM for 100 epochs
    som.train(data, epochs=100)

    # Visualize the result
    som.visualize(data)
    
output - one graph
  
  """)