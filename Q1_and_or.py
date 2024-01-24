print("""
class MPN:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def activate(self, inputs):
        weighted_sum = sum(inputs[i] * self.weights[i] for i in range(len(inputs)))
        return 1 if weighted_sum >= self.threshold else 0
#AND Logic Functions

and_weights = [1, 1]
and_thresh = 2
and_neuron = MPN(and_weights, and_thresh)

#OR Logic Functions

or_weights = [1, 1]
or_thresh = 1
or_neuron = MPN(or_weights, or_thresh)

#Test AND Logic Functions

input_and = [(0, 0), (1, 0), (0, 1), (1, 1)]
print('AND logic function:')
for i in input_and:
    out = and_neuron.activate(i)
    print(f"input:{i}------> output:{out}")
#Test OR Logic Functions

input_or = [(0, 0), (1, 0), (0, 1), (1, 1)]
print('OR logic function:')
for i in input_or:
    out = or_neuron.activate(i)
    print(f"input:{i}------> output:{out}")
  
  
  
output - 
AND logic function:
input:(0, 0)------> output:0
input:(1, 0)------> output:0
input:(0, 1)------> output:0
input:(1, 1)------> output:1
OR logic function:
input:(0, 0)------> output:0
input:(1, 0)------> output:1
input:(0, 1)------> output:1
input:(1, 1)------> output:1
  
  
  
  
  
  
  
  """)