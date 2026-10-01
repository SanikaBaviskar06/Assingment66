import math

actual = [1, 0, 1, 1]
predicted = [0.9, 0.2, 0.8, 0.7]

mse = 0

for i in range(len(actual)):
    mse = mse + (actual[i] - predicted[i]) ** 2

mse = mse / len(actual)

bce = 0

for i in range(len(actual)):
    bce = bce + (
        actual[i] * math.log(predicted[i])
        + (1 - actual[i]) * math.log(1 - predicted[i])
    )

bce = -bce / len(actual)

print("Actual Values :", actual)
print("Predicted Values :", predicted)
print("Mean Squared Error :", mse)
print("Binary Cross Entropy :", bce)