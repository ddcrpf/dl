print("""
import numpy as np

class HoppfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        for pattern in patterns:
            pattern = np.array(pattern)
            outer_product = np.outer(pattern, pattern)
            np.fill_diagonal(outer_product, 0)
            self.weights += outer_product

    def energy(self, state):
        state = np.array(state)
        return -0.5 * np.dot(state, np.dot(self.weights, state))

    def update_rule(self, state):
        new_state = np.sign(np.dot(self.weights, state))
        new_state[new_state >= 0] = 1
        new_state[new_state < 0] = 0
        return new_state

    def run(self, initial_state, max_iterations=100):
        current_state = np.array(initial_state)
        for _ in range(max_iterations):
            new_state = self.update_rule(current_state)
            if np.array_equal(new_state, current_state):
                break
            current_state = new_state
        return current_state

pattern_size = 4
hopp_net = HoppfieldNetwork(pattern_size)
training_pattern = [[1, 1, 1, -1]]
hopp_net.train(training_pattern)
initial_state = [0, 0, 1, 0]
result = hopp_net.run(initial_state)
print("initial state:", initial_state)
print("final state:", result)
print("energy of final state :", hopp_net.energy(result))

output - 
initial state: [0, 0, 1, 0]
final state: [1. 1. 1. 0.]
energy of final state : -3.0

  """)