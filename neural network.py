import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Neural Network function
def neural_network(x1, x2, w1, w2, bias):
    weighted_sum = (x1 * w1) + (x2 * w2) + bias
    output = sigmoid(weighted_sum)
    return output

# Input values
x1 = 1
x2 = 0

# Weights and bias
w1 = 0.8
w2 = 0.4
bias = -0.3

# Compute output
result = neural_network(x1, x2, w1, w2, bias)

print("Neural Network Output =", result)