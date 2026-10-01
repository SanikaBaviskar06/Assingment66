x = 2
weight = 0.5
bias = 0.1

target = 1
learning_rate = 0.1

prediction = (x * weight) + bias

error = target - prediction

gradient = error * x

old_weight = weight

weight = weight + (learning_rate * gradient)

print("Input :", x)
print("Target :", target)
print("Prediction :", prediction)
print("Error :", error)
print("Old Weight :", old_weight)
print("Updated Weight :", weight)