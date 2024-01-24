print("""
class MPN:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def activate(self, inputs):
        weighted_sum = sum(inputs[i] * self.weights[i] for i in range(len(inputs)))
        return 1 if weighted_sum >= self.threshold else 0

andnot_weights = [1, -1]
andnot_thresh = 1
andnot_neuron = MPN(andnot_weights, andnot_thresh)

input_andnot = [(0, 0), (1, 0), (0, 1), (1, 1)]
print('AND-NOT logic function:')
for i in input_andnot:
    out = andnot_neuron.activate(i)
    print(f"input:{i}------> output:{out}")

nand_weights = [-1, -1]
nand_thresh = -1
nand_neuron = MPN(nand_weights, nand_thresh)

or_weights = [1, 1]
or_thresh = 1
or_neuron = MPN(or_weights, or_thresh)

xor_weights = [1, 1]
xor_thresh = 2
xor_neuron = MPN(xor_weights, xor_thresh)

input_xor = [(0, 0), (1, 0), (0, 1), (1, 1)]
print('XOR logic function:')
for i in input_xor:
    out = xor_neuron.activate((nand_neuron.activate(i), or_neuron.activate(i)))
    print(f"input:{i}------> output:{out}")
    
    
output - 

AND-NOT logic function:
input:(0, 0)------> output:0
input:(1, 0)------> output:1
input:(0, 1)------> output:0
input:(1, 1)------> output:0
XOR logic function:
input:(0, 0)------> output:0
input:(1, 0)------> output:1
input:(0, 1)------> output:1
input:(1, 1)------> output:0

  """)