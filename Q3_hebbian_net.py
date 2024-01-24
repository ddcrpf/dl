print("""
#Lab4:Write a program to implement Hebb Net to classify two dimensional input patterns
import numpy as np
import matplotlib.pyplot as plt

class HebbianNetwork:
    def __init__(self, input_size):
        self.weights = np.zeros((input_size, input_size))

    def train(self, input_patterns):
        for pattern in input_patterns:
            self.weights += np.outer(pattern, pattern)

    def classify(self, input_pattern):
        output = np.dot(input_pattern, self.weights)
        return np.sign(output)

def plot_patterns(input_patterns, title):
    for pattern in input_patterns:
        plt.scatter(pattern[0], pattern[1], color='b')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.show()

def main():
    input_size = 2
    hebb_net = HebbianNetwork(input_size)

    # Define input patterns
    pattern1 = np.array([1, 1])
    pattern2 = np.array([1, -1])
    pattern3 = np.array([-1, 1])
    pattern4 = np.array([-1, -1])

    input_patterns = [pattern1, pattern2, pattern3, pattern4]

    # Train the Hebbian network
    hebb_net.train(input_patterns)

    # Classify new patterns
    test_pattern1 = np.array([0.5, 0.5])
    test_pattern2 = np.array([0.5, -0.5])
    test_pattern3 = np.array([-0.5, 0.5])
    test_pattern4 = np.array([-0.5, -0.5])

    result1 = hebb_net.classify(test_pattern1)
    result2 = hebb_net.classify(test_pattern2)
    result3 = hebb_net.classify(test_pattern3)
    result4 = hebb_net.classify(test_pattern4)

    print(f"Test Pattern 1 Result: {result1}")
    print(f"Test Pattern 2 Result: {result2}")
    print(f"Test Pattern 3 Result: {result3}")
    print(f"Test Pattern 4 Result: {result4}")

    # Plot input patterns and test patterns
    plot_patterns(input_patterns, 'Input Patterns')
    plot_patterns([test_pattern1, test_pattern2, test_pattern3, test_pattern4], 'Test Patterns')

if __name__ == "__main__":
    main()
    
    
output - includes graph
Test Pattern 1 Result: [1. 1.]
Test Pattern 2 Result: [ 1. -1.]
Test Pattern 3 Result: [-1.  1.]
Test Pattern 4 Result: [-1. -1.]

  """)